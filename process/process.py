
class Process(object):
    """
    This Class provides the basic functionality for biological processes. 
    It defines the simulation-process-interface:

    - id
    - name
    - index
    - Resource requirements



    Provides methods to:

    - copy/write state from/to simulation

    """

    def __init__(self, id, name):
        """
        Inits main attributes. Subclasses will initialize all parameters and constants from the database.
        """
        self.id = id
        self.name = name


        # Need to be implemented as lists in subclasses
        self.__substrate_whole_cell_ids = []

        self.__substrates = []

        # to be filled with the actual states
        self.metabolite = []
        self.rna = []
        self.protein = []
        self.states = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def store_object_refs(self, simulation):
        """
        Store states inside process.

        :param simulation:
        :return:
        """
        self.metabolite = simulation.get_state("Metabolite")
        self.rna = simulation.get_state("Rna")
        self.protein = simulation.get_state("Protein")
        self.states = [self.metabolite, self.rna, self.protein]

    def initialize_constants(self, knowledgebase, simulation, opts):
        """
        Read the data from the knowledgebase.

        :param knowledgebase:
        :param simulation:
        :param opts:
        :return: None
        """
        self.__wholeCellModelIds


    def copy_from_state(self):
        """

        :param stimulus:
        :return:
        """
        self.__substrates = self._copy_substrates_from_state()

    def _copy_substrates_from_state(self):
        for id in self.__substrate_whole_cell_ids:
            if id in self.metabolite.whole_cell_ids:
                self.__substrates[id] = self.metabolite.counts[id]
            if id in self.rna.whole_cell_ids:
                self.__substrates[id] = self.rna.counts[id]
            if id in self.protein.whole_cell_ids:
                self.__substrates[id] = self.protein.counts[id]

    def copy_to_state(self):
        """

        :return:
        """
        self._copy_substrates_to_state()

    def _copy_substrates_to_state(self):
        for id in self.__substrate_whole_cell_ids:
            if id in self.metabolite.whole_cell_ids:
                self.metabolite.counts[id] = self.__substrates[id]
            if id in self.rna.whole_cell_ids:
                self.rna.counts[id] = self.__substrates[id]
            if id in self.protein.whole_cell_ids:
                self.protein.counts[id] = self.__substrates[id]

    def evolve_state(self):
        """
        Abstract, needs to be implemented in subclass.
        :return:
        """
        pass

