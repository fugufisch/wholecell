__author__ = 'max'

from state import State
import sys
from data.knowledgebase import Knowledgebase

class SingleGene(State, object):
    """
    Storing the information related to each single gene of the database
    """
    def __init__(self, gene_by_row):
        super(SingleGene, self).__init__(gene_by_row["WholeCellModelID"], gene_by_row["Name"])
        self.__type = None
        self.__count = None  # ??
        self.__coordinate = None
        self.__length = None
        self.__sequence = None
        self._set_information(gene_by_row)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def count(self):
        return self.__count

    @type.setter
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
        if gene_by_row.Type:
            self.type = gene_by_row.Type
        if gene_by_row.Coordinate:
            self.coordinate = gene_by_row.Coordinate
        if gene_by_row.Length:
            self.length = gene_by_row.Length
        if gene_by_row.Sequence:
            self.sequence = gene_by_row.Sequence

class Gene(State, dict, object):
    """
    A dictionary containing all genes of the system
    """
    def __init__(self, init_dict):
        super(Gene, self).__init__(init_dict["ID"], init_dict["name"])
        #super(Gene, self).__init__()

        self.kb = Knowledgebase(data_dir='../data', select_states=["genes"])  # get only the gene information
        for i in range(len(self.kb.states.genes["WholeCellModelID"])):  # iter over all genes
            self.add_gene(self.kb.states.genes.transpose()[i]) # get the complete ith row

    def add_gene(self, gene_by_row):
        """
        This function adds a gene, as long as it does not already exist, to the gene dictionary
        @param gene_by_row: panda object containing the row information of a gene
        @return:None
        """
        if gene_by_row.WholeCellModelID not in self:
            self[gene_by_row.WholeCellModelID] = SingleGene(gene_by_row)  # append each Single gene to a list of genes
        else:
            print "{0} already known".format(gene_by_row.WholeCellModelID)

    def remove_gene(self, WholeCellModelID):
        """
        Remove a gene from the dictonary
        @param WholeCellModelID: str identifier
        @return:
        """
        if WholeCellModelID in self:
            del self[WholeCellModelID]


    def get_gene(self, WholeCellModelID):
        """
        Get a gene from the dictionary
        @param WholeCellModelID:
        @return: SingleGene object if key in dictionary
        @return: None if key not in dictionary
        """
        if WholeCellModelID in self:
            return self[WholeCellModelID]
        else:
            return None


if __name__ == "__main__":
    Gene({"ID": 1, "name":"gene"})