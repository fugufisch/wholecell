import state

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

        self._construct_states()
        self._construct_processes()


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

    def _construct_states(self):
        """
        instantiate state objects according to the specification
        :return:
        """
        state_objects = {}
        for s in self.states:
            package_name = "state.{0}".format(s["type"].lower())
            state_package = __import__(package_name)
            state_module = getattr(state_package, s["type"].lower())
            state_type = getattr(state_module, s["type"])

            state_objects[s["ID"]] = state_type(s)

        self.states = state_objects

    def _construct_processes(self):
        """
        instantiate state objects according to the specification
        :return:
        """
        process_objects = {}
        for s in self.processes:
            package_name = "process.{0}".format(s["type"].lower())
            process_package = __import__(package_name)
            process_module = getattr(process_package, s["type"].lower())
            process_type = getattr(process_module, s["type"])
            process_objects[s["ID"]] = process_type(s)

        self.processes = process_objects
