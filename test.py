__author__ = 'max'

import csv
import simulation

states = csv.DictReader(open("data/states.csv", "r"))
processes = csv.DictReader(open('data/processes.csv', "r"))

s = simulation.Simulation(processes, states, 100)