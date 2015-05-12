class Simulation(object):
    """
    Model simulation class
    - Runs simulations
    - Stores and loads simulation data
    """
    def __init__(self, processes, states, steps):
        """
        Sets up simulation and links processes and states.

        :type steps: int
        :param processes: List of Process objects
        :param states: List of State objects
        :return: None
        """
        super(Simulation, self).__init__()
        self.processes = processes
        self.states = states
        self.steps = steps


    def evolve_state(self):
        """
        Simulate the next step.

        :rtype : tuple
        :param requirements: list of Requirements for each process
        :return: metabolite usage in current state
        """
        requirements = [] # what processes need
        usages = [] # what was used in this step

        for p in self.processes:
            p.copy_from_state()
            p.copy_to_state()


        return (requirements, usages)


    def run(self, loggers):
        """
        Run and log the simulation

        :param loggers:
        :return:
        """
        metabolite = self.states["metabolite"]
        for step in xrange(self.steps):
            req, usages = self.evolve_state
            metabolite.requirements = req
            metabolite.usages = usages


