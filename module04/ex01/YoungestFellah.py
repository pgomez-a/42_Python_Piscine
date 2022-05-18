import pandas as pd

def youngest_fellah(dataset, year):
    """
    Returns a dictionary containing the age of the youngest woman and man
    who took part in the Olympics on that year.
    """
    output = dict()
    male_targets = dataset.loc[dataset["Year"] == year].loc[dataset["Sex"] == "M"]
    female_targets = dataset.loc[dataset["Year"] == year].loc[dataset["Sex"] == "F"]
    output["f"] = female_targets["Age"].min()
    output["m"] = male_targets["Age"].min()
    return output
