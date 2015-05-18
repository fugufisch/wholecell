import math
from data.knowledgebase import Knowledgebase
from state import State

__author__ = 'max'
__author__ = 'Sebastian'

class SingleMetabolite(State, object):
    """"""

    def __init__(self, metabolite_by_row):
        """Constructor for SingleMetabolite"""
        super(SingleMetabolite, self).__init__(metabolite_by_row["WholeCellModelID"], metabolite_by_row["Name"])

        self.__charge = float('nan')
        self.__molecularWeightCalc = None #float('nan')
        self.__exchangeLowerBound = float('nan')
        self.__exchangeUpperBound = float('nan')
        self.__reactions = None
        self.__volume = float('nan')
        self.__category = None

        self._set_information(metabolite_by_row)

    @property
    def charge(self):
        return self.__charge

    @charge.setter
    def charge(self, charge):
        self.__charge = charge

    @property
    def molecularWeightCalc(self):
        return self.__molecularWeightCalc

    @molecularWeightCalc.setter
    def molecularWeightCalc(self, molecularWeightCalc):
        self.__molecularWeightCalc = molecularWeightCalc

    @property
    def exchangeLowerBound(self):
        return self.__exchangeLowerBound

    @exchangeLowerBound.setter
    def exchangeLowerBound(self, exchangeLowerBound):
        self.__exchangeLowerBound = exchangeLowerBound

    @property
    def exchangeUpperBound(self):
        return self.__exchangeUpperBound

    @exchangeUpperBound.setter
    def exchangeUpperBound(self, exchangeUpperBound):
        self.__exchangeUpperBound = exchangeUpperBound

    @property
    def reactions(self):
        return self.__reactions

    @reactions.setter
    def reaction(self, reaction):
        self.__reactions = reaction

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        self.__category = category

    def _set_information(self, metabolite_by_row):
        if not math.isnan(metabolite_by_row.Charge):
            self.charge = metabolite_by_row.Charge
        if not math.isnan(metabolite_by_row.MolecularWeightCalc):
            self.molecularWeightCalc = metabolite_by_row.MolecularWeightCalc
        if not math.isnan(metabolite_by_row.ExchangeLowerBound):
            self.exchangeLowerBound = metabolite_by_row.ExchangeLowerBound
        if not math.isnan(metabolite_by_row.ExchangeUpperBound):
            self.exchangeUpperBound = metabolite_by_row.ExchangeUpperBound
        if isinstance(metabolite_by_row.Reactions, str):
            self.reaction = metabolite_by_row.Reactions.split(";")
        if not math.isnan(metabolite_by_row.Volume):
            self.volume = metabolite_by_row.Volume
        if metabolite_by_row.Category:
            self.category = metabolite_by_row.Category

class Metabolite(State, dict, object):
    """
    Metabolites
    """
    def __init__(self, init_dict, knowledgebase):
        super(Metabolite, self).__init__(init_dict["ID"], init_dict["name"], knowledgebase)

        #self.kb = Knowledgebase(data_dir='../data', select_states=["metabolites"])  # get only the gene information
        #for i in range(len(self.kb.states.metabolites["WholeCellModelID"])):  # iter over all genes
        #    print self.kb.states.metabolites.transpose()[i]  # get the line/gene information
        #    self.add_metabolite(self.kb.states.metabolites.transpose()[i])  # get the complete ith row

    def add_metabolite(self, metabolite_by_row):
        """
        This function adds a metabolite to the metabolite dictionary
        @param metabolite_by_row: panda object containing the row information of a gene
        @return: None
        """
        if metabolite_by_row.WholeCellModelID not in self and isinstance(metabolite_by_row.WholeCellModelID, str):
            self[metabolite_by_row.WholeCellModelID] = SingleMetabolite(metabolite_by_row)  # append each Single gene to a list of genes
        elif isinstance(metabolite_by_row.WholeCellModelID, str):
            print "WholeCellModelID {0} already known".format(metabolite_by_row.WholeCellModelID)
        else:
            print "Something strange WholeCellModelID: {0}".format(metabolite_by_row.WholeCellModelID)
if __name__ == "__main__":
    Metabolite(({"ID": 2, "name":"metabolite"}))