import pandas as pd

class SpatioTemporalData(object):
    def __init__(self, dataset):
        """
        It takes a dataset (pandas.DataFrame) as argument.
        """
        self.dataset = dataset
        return

    def when(self, location):
        """
        Returns a list containing the years where games were held
        in the given location.
        """
        output = list()
        targets = self.dataset.loc[self.dataset["City"] == location]
        for y,x in targets.iterrows():
            if x["Year"] not in output:
                output.append(x["Year"])
        return output

    def where(self, date):
        """
        Returns the location where the Olympics took place in the given year.
        """
        output = list()
        targets = self.dataset.loc[self.dataset["Year"] == date]
        for y,x in targets.iterrows():
            if x["City"] not in output:
                output.append(x["City"])
        return output
