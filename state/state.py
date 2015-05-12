__author__ = 'max'

class State(object):
    """
    Generic cell state objects. These can be used and produced by processes during simulation.
    """

    def __init__(self, id, name):
        """
        Initialize object.
        :param id: str
        :param name: str
        :return: None
        """
        self.id = id
        self.name = name

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

    def initializeConstants(self, input, simulation):
        """
        Initialize the values of parameters.

        :param input: Initializer
        :param simulation:
        :return: None
        """
        self.parameters = input.get_parameters(self.id)