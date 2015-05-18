__author__ = 'max'

from state import State

class Protein(State):
    def __init__(self, init_dict, knowledgebase):
        super(Protein, self).__init__(init_dict["ID"], init_dict["name"], knowledgebase)
