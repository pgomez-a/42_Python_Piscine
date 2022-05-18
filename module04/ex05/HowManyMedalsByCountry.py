import pandas as pd

def how_many_medals_by_country(dataset, country):
    """
    It returns a dictionary of dictionaries giving the number and type of medal
    for each competition where the country delegation earned medals.
    """
    output = dict()
    target = dataset.loc[dataset["Team"] == country]
    target.drop_duplicates("Name")
    for y,x in target.iterrows():
        if x["Year"] not in output:
            medals = {'G':0, 'S':0, 'B':0}
        if x["Medal"] == "Gold":
            medals['G'] += 1
        elif x["Medal"] == "Silver":
            medals['S'] += 1
        elif x["Medal"] == "Bronze":
            medals['B'] += 1
        output[x["Year"]] = medals.copy()
    return output
