from state import State
__author__ = 'max'

class ChromosomeSequence(object):
    def __init__(self):
        """

        """
        pass

    def randomChromosome(self, length):
        pass


class Chromosome(State, object):
    """

    """
    def __init__(self, id, name):
        """

        @return:
        """
        super(Chromosome, self).__init__(id, name)
        self.__gene = None
        self.__metabolite = None
        self.__sequence = None
        self.__sequence_len = None
        self.__transcript = None

    @property
    def transcript(self):
        return self.__transcript

    @transcript.setter
    def transcript(self, transcript):
        self.__transcript = transcript

    @property
    def gene(self):
        return self.__gene

    @gene.setter
    def gene(self, gene):
        self.__gene = gene

    @property
    def metabolite(self):
        return self.__metabolite

    @metabolite.setter
    def metabolite(self, metabolite):
        self.__metabolite = metabolite

    def storeObjectReferences(self, simulation):
        self.gene = simulation.gene
        self.metabolite = simulation.state('Metabolite');
        self.transcript = simulation.state('Transcript');

    def initializeConstants(self, input, simulation):
        chr_seq = ChromosomeSequence()
        chr_seq.randomChromosome()


if __name__ == "__main__":
    chr = Chromosome("a","a")