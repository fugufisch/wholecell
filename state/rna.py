__author__ = 'max'

from state import State

class Rna(State):
    def __init__(self, init_dict):
        super(Rna, self).__init__(init_dict["ID"], init_dict["name"])