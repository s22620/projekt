import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualization:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self, column):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column], kde=True)
        plt.title(f'Histogram of {column}')
        plt.show()

    def plot_scatter(self, x_column, y_column):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.data, x=x_column, y=y_column)
        plt.title(f'Scatter plot of {x_column} vs {y_column}')
        plt.show()
