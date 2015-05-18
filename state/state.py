__author__ = 'max'
__author__ = 'Sebastian'

class State(object):
    """
    Generic cell state objects. These can be used and produced by processes during simulation.
    """

    def __init__(self, id, name, knowledgebase):
        """

        @param id: state id
        @param name: state name

        """
        self.__id = id
        self.__name = name

        self._initializeConstants(knowledgebase)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def parameters(self):
        return self.parameters

    @parameters.setter
    def parameters(self, value):
        self.parameters = value

    @property
    def options(self):
        return self.options

    @options.setter
    def options(self, value):
        self.options = value

    # do not change this is a abstract function to remember that this function has to be implemented in all classes
    # which inherit from State
    def storeObjectReferences(self, simulation):
        pass

    def _initializeConstants(self, knowledgebase):
        """
        @param knowledgebase:
        @param simulation:
        @return:
        """
        ids = getattr(knowledgebase.states, self.__id.lower()+"s").WholeCellModelID
        self._counts = dict(zip(ids, [1]*len(ids)))