__author__ = 'jannis'

import pandas, os

class dummy(object):
    """ an empty class used to define the states and processes attribute in the knowledgebase """
    pass

class Knowledgebase(object):
    """
    This class provides convenient access to data which is required to instantiate states and processes.

    """

    states_names = ['genes',
                    'metabolites',
                    'transcriptional_units']

    processes_names = []

    def __init__(self, data_dir='data', select_states=states_names, select_processes=processes_names):
        self._data_dir = data_dir
        # initialize scaffold for states and processes tree
        self.states = dummy()
        self.processes = dummy()

        self.states_names = select_states

        # get the data tables for states and processes
        for tp in ['states', 'processes']:
            # iterate over the state_names and process_names
            for name in getattr(self, '%s_names' %(tp)):
                # get the data table
                table = self._get_data_table(name)
                # get the self.state or self.process handle
                tp_handle = getattr(self, tp)
                # store data table in self.process or self.state
                setattr(tp_handle, name, table)

    def _get_data_table(self, name):
        """
        function to get a data table for a process or a state
        :param name: name of process/state
        :return: pandas data frame
        """
        # check if a specific handler is available for that table
        if hasattr(self, '_parse_'+name):
            data = getattr(self, '_parse_'+name)()
        else:  # if not use default handler
            data = self._default_handler(name)
        return data

    def _default_handler(self, name):
        """
        default handler for data tables
        :param name: name of the process/state
        :return:
        """
        try:
            file_path = os.path.join(self._data_dir, 'wcm_%s.csv' %(name))
            df = pandas.read_csv( file_path, sep=';', decimal=',')
            return df
        except IOError:
            raise Exception('Error: No data table found for %s' %(name))

    def _parse_genes(self):
        """
        example of a specific parsing function (to be used instead of the default parsing)
        specific parsing method for the gene state
        :return: pandas data frame
        """
        df = self._default_handler('genes')
        df['HalfLifeMean'] = (df['HalfLifeExp'] + df['HalfLifeCalc'])/2
        return df