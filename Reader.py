import pandas


class Reader():

    def __init__(self, filepath):

        self.filepath = filepath

    def read(self, filepath):

        filename = pandas.read_csv(filepath, sep=';')

        return filename
