__author__ = 'max'
__author__ = "Sebastian"

class MonomerInformation(object):
    """"""

    def __init__(self, monomer_by_row):
        """Constructor for MonomerInformation"""
        self.__whole_cell_model_id = None
        self.__name = None
        self.__molecular_weight
        self.__gene = None
        self.__length =  None
        self.__sequence = None
        self.__half_life = None
        self.__instability = None
        self.__stability = None
        self.__counts = None

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
    def gene(self):
        return self.__gene

    @gene.setter
    def gene(self, gene):
        self.__gene = gene

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

    @property
    def half_life(self):
        return self.__half_life

    @half_life.setter
    def half_life(self, half_life):
        self.__half_life = half_life

    @property
    def instability(self):
        return self.__instability

    @instability.setter
    def instability(self, instability):
        self.__instability = instability

    @property
    def stability(self):
        return self.__stability

    @stability.setter
    def stability(self, stability):
        self.__stability = stability

class ProteinMonomer(object):
    """Class for protein monomers"""

    def __init__(self, init_dict):
        """Constructor for ProteinMonomer"""
        super(ProteinMonomer, self).__init__(init_dict["ID"], init_dict["name"])
        
# fixed Constant names  %names of process properties that are considered fixed constants
#     'molecularWeights';
# 'baseCounts';
# 'lengths';
# 'halfLives';
# minimumAverageExpression
# 
# statename
# 
# counts %names of properties which are part of the simulation's state

    def storedObjectReference(self,simulation):
        self.gene = simulation.state("gene")
        self.ribosome = simulation.state("ribosome")

    def initializeConstants(self, knowledgeBase, simulation):
        
        num_monomers = #from knowledgebase

    def get_monomer(self):
        pass