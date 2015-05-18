__author__ = 'max'
__author__ = 'Sebastian'

import math
from state import State
from data.knowledgebase import Knowledgebase

class MetaboliteInformation(object):
    """"""

    def __init__(self, metabolite_by_row):
        """Constructor for SingleMetabolite"""
        #super(SingleMetabolite, self).__init__(metabolite_by_row["WholeCellModelID"], metabolite_by_row["Name"])
        self.__name  = None
        self.__WholeCellModelID = None
        self.__charge = float('nan')
        self.__molecularWeightCalc = None #float('nan')
        self.__exchangeLowerBound = float('nan')
        self.__exchangeUpperBound = float('nan')
        self.__reactions = None
        self.__volume = float('nan')
        self.__category = None

        self._set_information(metabolite_by_row)

    @property
    def WholeCellModelID(self):
        return self.__WholeCellModelID

    @WholeCellModelID.setter
    def WholeCellModelID(self, WholeCellModelID):
        self.__WholeCellModelID = WholeCellModelID

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

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
        self.WholeCellModelID = metabolite_by_row.whole_cell_model_id
        self.name = metabolite_by_row.Name
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
        super(Metabolite, self).__init__(init_dict["ID"], init_dict["name"])
        self.__knowledgebase = knowledgebase

    def remove_metabolite(self, WholeCellModelID):
        """
        Remove a metabolite from the dictionary
        @param WholeCellModelID: str identifier
        @return:
        """
        if WholeCellModelID in self:
            del self[WholeCellModelID]

    def initialize_all_metabolite(self):
        """
        This function adds a metabolite to the metabolite dictionary
        @param metabolite_by_row: panda object containing the row information of a gene
        @return: None
        """
        for i in range(len(self.__knowledgebase.metabolites)):
            metabolite_by_row = self.__knowledgebase.metabolites.iloc[i]
            if metabolite_by_row.whole_cell_model_id not in self and isinstance(metabolite_by_row.whole_cell_model_id, str):
                self[metabolite_by_row.whole_cell_model_id] = MetaboliteInformation(metabolite_by_row)  # append each Single gene to a list of genes
            elif isinstance(metabolite_by_row.whole_cell_model_id, str):
                print "WholeCellModelID {0} already known".format(metabolite_by_row.whole_cell_model_id)
            else:
                print "Something strange WholeCellModelID: {0}".format(metabolite_by_row.whole_cell_model_id)

    def initialize_metabolite(self, WholeCellModelID):
        """
        initialisation of specific metabolites
        @param WholeCellModelID:
        @return:
        """

        metabolite_by_row = self.__knowledgebase.metabolites[self.__knowledgebase.metabolites.whole_cell_model_id == WholeCellModelID]
        if len(metabolite_by_row) == 1:
            metabolite_by_row = metabolite_by_row.iloc[0]
            if metabolite_by_row.whole_cell_model_id not in self:
                self[metabolite_by_row.whole_cell_model_id] = MetaboliteInformation(metabolite_by_row)  # append each Single gene to a list of genes
                pass
            else:
                print "{0} already known".format(WholeCellModelID)
        elif len(gene_by_row) > 1:
            print "{0} is {1} time in knowledgebase".format(WholeCellModelID, len(metabolite_by_row))
        else:
            print "{0} not in knowledgebase".format(WholeCellModelID)

if __name__ == "__main__":
    knowledgebase = Knowledgebase('../data')
    met = Metabolite({"ID": 2, "name":"metabolite"}, knowledgebase.states)
    #met.initialize_all_metabolite()
    met.initialize_metabolite("ADP")
    pass