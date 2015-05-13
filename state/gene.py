__author__ = 'max'

from state import State

class Gene(State):
    def __init__(self, init_dict):
        super(Gene, self).__init__(init_dict["ID"], init_dict["name"])
        