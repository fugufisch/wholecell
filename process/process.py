
class Process:
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

    def __init__(self, id, name, index):
        """
        Inits main attributes. 
        """
        self._id = id
        self._name = name
        self._index = index


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

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    def storeObjectRefs(self, simulation):
        """
        Communicate with simulation

        :param simulation:
        :return:
        """
        pass

    def copyFromState(self, stimulus):
        """

        :param stimulus:
        :return:
        """
        pass