import pandas as pd

def proportion_by_sport(dataset, year, sport, gender):
    """
    Displays the proportion of participants who played a given sport,
    among the participants of a given genders.
    """
    sample = dataset.loc[dataset["Year"] == year].loc[dataset["Sex"] == gender]
    sample = sample.drop_duplicates("Name")
    sample_tot = sample.shape[0]
    targets = sample.loc[dataset["Sport"] == sport]
    targets_tot = targets.shape[0]
    return targets_tot / sample_tot
