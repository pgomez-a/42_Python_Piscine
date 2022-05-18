import pandas as pd

class FileLoader(object):
    def load(self, path):
        """
        Takes as an argument the file path of the dataset to load.
        """
        output = pd.read_csv(path)
        shape = output.shape
        print("Loading dataset of dimensions {} x {}".format(shape[0], shape[1]))
        return output

    def display(self, df, n):
        """
        Displays the first n rows of the dataset if n is positive,
        or the last n rows if n is negative.
        """
        shape = df.shape[0]
        if n >= 0:
            print(df.loc[:n - 1,:])
        else:
            print(df.loc[shape + n:,:])
