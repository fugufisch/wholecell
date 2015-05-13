__author__ = 'max'


class Initializer(object):
    """
    Reads initial values from a file and provides an interface to the simulation class for initialization
    """
    def __init__(self):
        pass

    @property
    def parameters(self):
        return self.parameters

    @parameters.getter
    def parameters(self, id):
        return self.parameters[id]

