import state

class Simulation(object):
    """
    Model simulation class
    - Runs simulations
    - Stores and loads simulation data
    """
    def __init__(self, processes, states, knowledgebase, steps):
        """
        Sets up simulation and links processes and states.

        :type steps: int
        :param processes: List of Process objects
        :param states: List of State objects
        :return: None
        """
        super(Simulation, self).__init__()

        self.__processes = processes
        self.__states = states
        self.__knowledgebase = knowledgebase
        self.steps = steps

        self._construct_states()
        self._construct_processes()

    def get_state(self, id):
        """
        Get the state object 'id'.

        :param id: wholeCellId
        :return: state object
        """
        assert isinstance(id, str)
        return self.__states[id]

    def get_process(self, id):
        """
        Get the state object 'id'.

        :param id: wholeCellId
        :return: process object
        """
        assert isinstance(id, str)
        return self.__processes[id]

    def evolve_state(self):
        """
        Simulate the next step.

        :rtype : tuple
        :param requirements: list of Requirements for each process
        :return: metabolite usage in current state
        """
        requirements = [] # what processes need
        usages = [] # what was used in this step

        for p in self.__processes:
            p.copy_from_state()
            p.copy_to_state()


        return (requirements, usages)

    def run(self, loggers):
        """
        Run and log the simulation

        :param loggers:
        :return:
        """
        metabolite = self.__states["metabolite"]
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
        for s in self.__states:
            package_name = "state.{0}".format(s["ID"].lower())
            state_package = __import__(package_name)
            state_module = getattr(state_package, s["ID"].lower())
            state_name = getattr(state_module, s["ID"])

            state_objects[s["ID"]] = state_name(s, self.__knowledgebase.states)

        self.__states = state_objects

    def _construct_processes(self):
        """
        instantiate state objects according to the specification
        :return:
        """
        process_objects = {}
        for s in self.__processes:
            package_name = "process.{0}".format(s["ID"].lower())
            process_package = __import__(package_name)
            process_module = getattr(process_package, s["ID"].lower())
            process_name = getattr(process_module, s["ID"])

            process_objects[s["ID"]] = process_name(s)

        self.__processes = process_objects
