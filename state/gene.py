__author__ = 'max'

from state import State
from data.knowledgebase import Knowledgebase


class GeneInformation(object):
    """
    Storing the information related to each single gene of the database
    """
    def __init__(self, gene_by_row):
        self.__whole_cell_model_id = None
        self.__name = None
        self.__type = None
        self.__count = None  # ??
        self.__coordinate = None
        self.__length = None
        self.__sequence = None
        self.__synthesis_rate = None
        self.__prob_rna_pol_binding = None
        self.__half_life_mean = None
        self.__transcription_unit = None
        self._set_information(gene_by_row)

    @property
    def transcription_unit(self):
        return self.__transcription_unit

    @transcription_unit.setter
    def transcription_unit(self, transcription_unit):
        self.__transcription_unit = transcription_unit
    @property
    def half_life_mean(self):
        return self.__half_life_mean

    @half_life_mean.setter
    def half_life_mean(self, half_life_mean):
        self.__half_life_mean = half_life_mean

    @property
    def synthesis_rate(self):
        return self.__synthesis_rate

    @synthesis_rate.setter
    def synthesis_rate(self, synthesis_rate):
        self.__synthesis_rate = synthesis_rate

    @property
    def prob_rna_pol_binding(self):
        return self.__prob_rna_pol_binding

    @prob_rna_pol_binding.setter
    def prob_rna_pol_binding(self, prob_rna_pol_binding):
        self.__prob_rna_pol_binding = prob_rna_pol_binding

    @property
    def whole_cell_model_id(self):
        return self.__whole_cell_model_id

    @whole_cell_model_id.setter
    def whole_cell_model_id(self, whole_cell_model_id):
        self.__whole_cell_model_id = whole_cell_model_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    @property
    def coordinate(self):
        return self.__coordinate

    @coordinate.setter
    def coordinate(self, coordinate):
        self.__coordinate = coordinate

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def sequence(self):
        return self.__sequence

    @sequence.setter
    def sequence(self, sequence):
        self.__sequence = sequence


    def _set_information(self, gene_by_row):
        self.whole_cell_model_id = gene_by_row.WholeCellModelID
        self.name = gene_by_row.Name
        if gene_by_row.Type:
            self.type = gene_by_row.Type
        if gene_by_row.Coordinate:
            self.coordinate = gene_by_row.Coordinate
        if gene_by_row.Length:
            self.length = gene_by_row.Length
        if gene_by_row.Sequence:
            self.sequence = gene_by_row.Sequence
        if gene_by_row.ProbRNAPolBinding:
            self.prob_rna_pol_binding = gene_by_row.ProbRNAPolBinding
        if gene_by_row.SynthesisRate:
            self.synthesis_rate = gene_by_row.SynthesisRate
        if gene_by_row.HalfLifeMean:
            self.half_life_mean = gene_by_row.HalfLifeMean
        if gene_by_row.TranscriptionUnit:
            self.transcription_unit = gene_by_row.TranscriptionUnit

class Gene(State, dict, object):
    """
    A dictionary containing all genes of the system
    """
    def __init__(self, init_dict):
        super(Gene, self).__init__(init_dict["ID"], init_dict["name"])


    def initialize_genes(self, knowledgebase):
        """
        This function adds a gene, as long as it does not already exist, to the gene dictionary
        """
        for i in range(len(knowledgebase.genes.WholeCellModelID.dropna())):
            gene_by_row = knowledgebase.genes.iloc[i] # get the complete ith row

            if gene_by_row.WholeCellModelID not in self:
                self[gene_by_row.WholeCellModelID] = GeneInformation(gene_by_row)  # append each Single gene to a list of genes
            else:
                print "{0} already known".format(gene_by_row.WholeCellModelID)


    def get_gene(self, whole_cell_model_id):
        """
        Get a gene from the dictionary
        @param whole_cell_model_id:
        @return: SingleGene object if key in dictionary
        @return: None if key not in dictionary
        """
        if whole_cell_model_id in self:
            return self[whole_cell_model_id]
        else:
            return None


if __name__ == "__main__":
    knowledgebase = Knowledgebase('../data')
    g = Gene({"ID": 1, "name":"gene"})
    g.initialize_genes(knowledgebase.states)
    pass