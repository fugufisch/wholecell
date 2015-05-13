
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
        self.substrates = []
        self.enzymes = []
        self.parameters = []

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
        self.gene = simulation.get_state("Rna")
        self.protein = simulation.get_state("Protein")

    def copy_from_state(self, stimulus):
        """

        :param stimulus:
        :return:
        """
        pass

    def copy_to_state(self):
        """

        :return:
        """
        self.state

    def evolve_state(self):
        """
        Abstract, needs to be implemented in subclass.
        :return:
        """
        pass

