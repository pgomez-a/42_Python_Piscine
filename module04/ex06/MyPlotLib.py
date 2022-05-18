import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class MyPlotLib(object):
    """
    This class implements different plotting methods.
    """
    @staticmethod
    def histogram(data, features):
        """
        Plots one histogram for each numerical feature in the list.
        """
        for item in features:
            plt.hist(data[item])
            plt.title(item)
            plt.grid(True)
            plt.show()
        return

    @staticmethod
    def density(data, features):
        """
        Plots the density curve of each numerical feature in the list.
        """
        pd.DataFrame(data[features]).plot(kind = "density")
        plt.show()
        return

    @staticmethod
    def pair_plot(data, features):
        """
        Plots a matrix of subplots.
        """
        pd.plotting.scatter_matrix(data[features])
        plt.show()
        return

    @staticmethod
    def box_plot(data, features):
        """
        Displays a box plot for each numerical variable in the dataset.
        """
        for item in features:
            data.boxplot(column = features)
            plt.show()
        return
