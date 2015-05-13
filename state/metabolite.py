__author__ = 'max'

from state import State


class Metabolite(State):
    """
    Metabolites
    """
    def __init__(self, init_dict):
        super(Metabolite, self).__init__(init_dict["ID"], init_dict["name"])

