__author__ = 'max'
import csv
import simulation
from data.knowledgebase import Knowledgebase

class Initializer(object):
    """
    Reads initial values from a file and provides an interface to the simulation class for initialization
    """
    def __init__(self):
        self._init_knowledgebase()
        self._init_states()
        self._init_processes()
        s = simulation.Simulation(self.processes, self.states, self.knowledgebase, 100)


    def _init_knowledgebase(self):
        self.knowledgebase = Knowledgebase('data/')

    def _init_states(self):
        self.states = csv.DictReader(open("data/states.csv", "r"))

    def _init_processes(self):
        self.processes = csv.DictReader(open('data/processes.csv', "r"))


    @property
    def parameters(self):
        return self.parameters

    @parameters.getter
    def parameters(self, id):
        return self.parameters[id]

if __name__ == "__main__":
    init = Initializer()