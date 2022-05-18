import pandas as pd

def how_many_medals(dataset, name):
    """
    Returns a dictionary of dictionaries giving the number and type
    of medals for each year during which the participant won medals.
    """
    output = dict()
    target = dataset.loc[dataset["Name"] == name]
    for y,x in target.iterrows():
        if x["Year"] not in output:
            medals = {'G':0, 'S':0, 'B':0}
        if x["Medal"] == "Gold":
            medals['G'] += 1
        elif x["Medal"] == "Silver":
            medals['S'] += 1
        elif x["Medal"] == "Bronze":
            medals['B'] += 1
        output[x["Year"]] = medals
    return output
