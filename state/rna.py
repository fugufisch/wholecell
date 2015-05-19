import re
import math
from data.knowledgebase import Knowledgebase
__author__ = 'max'
__author__ = 'Sebastian'

from state import State

class MatureRnaInformation(object):
    """Information about the mature RNA"""
 
    def __init__(self, rna_by_row, knowledge_genes):
        """Constructor for MatureRna"""
        self.__coordinate = None
        self.__direction = None
        self.__genes = None
        self.__length = None
        self.__name = None
        self.__prob_rna_pol_binding = None
        self.__sequence = None
        self.__synthesis_rate = None
        self.__whole_cell_model_id = None
        self.__type = None
        self.__expected_gene_expression = {}
        self.__expected_gene_half_life = {}


        self._set_information(rna_by_row)
        self._initializeConstants(knowledge_genes)
 # 'Promoter10Coordinate',
 # 'Promoter10Length',
 # 'Promoter35Coordinate',
 # 'Promoter35Length',
    @property
    def coordinate(self):
        return self.__coordinate

    @coordinate.setter
    def coordinate(self, coordinate):
        self.__coordinate = coordinate

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @property
    def genes(self):
        return self.__genes

    @genes.setter
    def genes(self, genes):
        self.__genes = genes

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def prob_rna_pol_binding(self):
        return self.__prob_rna_pol_binding

    @prob_rna_pol_binding.setter
    def prob_rna_pol_binding(self, prob_rna_pol_binding):
        self.__prob_rna_pol_binding = prob_rna_pol_binding

    @property
    def sequence(self):
        return self.__sequence

    @sequence.setter
    def sequence(self, sequence):
        self.__sequence = sequence

    @property
    def synthesis_rate(self):
        return self.__synthesis_rate

    @synthesis_rate.setter
    def synthesis_rate(self, synthesis_rate):
        self.__synthesis_rate = synthesis_rate

    @property
    def whole_cell_model_id(self):
        return self.__whole_cell_model_id

    @whole_cell_model_id.setter
    def whole_cell_model_id(self, whole_cell_model_id):
        self.__whole_cell_model_id = whole_cell_model_id

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def expected_gene_expression(self):
        return self.__expected_gene_expression

    @expected_gene_expression.setter
    def expected_gene_expression(self, expected_gene_expression):
        self.__expected_gene_expression = expected_gene_expression

    @property
    def expected_gene_half_life(self):
        return self.__expected_gene_half_life

    @expected_gene_half_life.setter
    def expected_gene_half_life(self, expected_gene_half_life):
        self.__expected_gene_half_life = expected_gene_half_life

    def _set_information(self, rna_by_row):

        if rna_by_row.Coordinate:
            self.coordinate = rna_by_row.Coordinate
        if rna_by_row.Direction:
            self.direction = rna_by_row.Direction
        if isinstance(rna_by_row.Genes,str):
            #print "rna_by_row.Genes: ", rna_by_row.Genes
            self.genes = re.findall("[MG_0-9]+", rna_by_row.Genes)
        if rna_by_row.Length:
            self.length = rna_by_row.Length
        if rna_by_row.Name:
            self.name = rna_by_row.Name
        if rna_by_row.ProbRNAPolBinding:
            self.prob_rna_pol_binding = rna_by_row.ProbRNAPolBinding
        if rna_by_row.Sequence:
            self.sequence = rna_by_row.Sequence
        if rna_by_row.SynthesisRate:
            self.synthesis_rate = rna_by_row.SynthesisRate
        if rna_by_row.Type:
            self.type = rna_by_row.Type
        if rna_by_row.WholeCellModelID:
            self.whole_cell_model_id = rna_by_row.WholeCellModelID

    def _initializeConstants(self, knowledge_genes):
        if len(self.genes) > 1:
            for gene_id in self.genes:
                gene_by_row = knowledge_genes[knowledge_genes.WholeCellModelID == gene_id]
                if not gene_by_row.empty:
                    self.expected_gene_half_life[gene_id] = gene_by_row.iloc[0].HalfLifeMean * 60  # experimental gen half life
                    self.expected_gene_expression[gene_id] = gene_by_row.iloc[0].Expression / sum(knowledge_genes.Expression.dropna())  # experimental gene expression

    def get_rna_decay_rate(self):
        """
        decay rate of RNAs (mol/s)
        @return:
        """
        return math.log(2) / self.half_life

class Rna(State, dict, object):
    def __init__(self, init_dict):
        super(Rna, self).__init__(init_dict["ID"], init_dict["name"])


        #expectedGeneExpression      %experimental gene expression
        #expectedGeneHalfLives       %experimental gene half lives

        #geneHalfLives %half lifes of each gene (s)
        #geneExpression %mol fractions of genes

    def initialize_all_rna(self, knowledgebase):
        """ initializing all rnas

        @param knowledgebase: pandas obj
        @return:
        """
        for i in range(len(knowledgebase.transcriptional_units.WholeCellModelID.dropna())):
            rna_by_row = knowledgebase.transcriptional_units.iloc[i] # get the complete ith row

            if rna_by_row.WholeCellModelID not in self:
                self[rna_by_row.WholeCellModelID] = MatureRnaInformation(rna_by_row, knowledgebase.genes)  # append each Single gene to a list of genes
            else:
                print "{0} already known".format(rna_by_row.WholeCellModelID)


    def initialize_rna(self, knowledgebase, whole_cell_model_id):
        """
        This function adds a rna, as long as it does not already exist, to the rna dictionary
        """
        rna_by_row = knowledgebase.transcriptional_units[knowledgebase.transcriptional_units.whole_cell_model_id == whole_cell_model_id]
        if len(rna_by_row) == 1:
            rna_by_row = rna_by_row.iloc[0]
            if rna_by_row.whole_cell_model_id not in self:
                self[rna_by_row.whole_cell_model_id] = MatureRnaInformation(rna_by_row, knowledgebase.genes)  # append each Single gene to a list of genes
                pass
            else:
                print "{0} already known".format(whole_cell_model_id)
        elif len(gene_by_row) > 1:
            print "{0} is {1} time in knowledgebase".format(whole_cell_model_id, len(rna_by_row))
        else:
            print "{0} not in knowledgebase".format(whole_cell_model_id)

    def get_expected_gene_decay_rates(self):
        return mat.log(2) / self.expected_gene_half_life

if __name__ == "__main__":
    knowledgebase = Knowledgebase('../data')
    r = Rna({"ID": 1, "name":"gene"})
    #r.initializeConstants(knowledgebase.states,"simulation")
    r.initialize_all_rna(knowledgebase.states)
    pass