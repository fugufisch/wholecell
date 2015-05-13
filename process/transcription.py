__author__ = 'max'

from process import Process

class Transcription(Process):
    def __init__(self, init_dict):
        super(Transcription, self).__init__(init_dict["ID"], init_dict["name"])