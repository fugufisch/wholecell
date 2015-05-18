import csv
from data.knowledgebase import Knowledgebase

__author__ = 'max'

import simulation

knowledgebase = Knowledgebase('data/')
processes = csv.DictReader(f=open('data/processes.csv', 'r'))
states = csv.DictReader(f=open('data/states.csv','r'))

s = simulation.Simulation(processes, states, knowledgebase, 100)
m = s.get_state('Metabolite')