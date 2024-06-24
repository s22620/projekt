import pandas as pd

class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def basic_statistics(self):
        return self.data.describe()

    def filter_data(self, column, value):
        return self.data[self.data[column] == value]

    def convert_categorical_to_numeric(self, column):
        self.data[column] = pd.factorize(self.data[column])[0]

    def sort_data(self, column, ascending=True):
        return self.data.sort_values(by=column, ascending=ascending)
