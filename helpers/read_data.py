import pandas as pd
def search_by_country(country, path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data, columns=["Country/Territory", "2022 Population","2020 Population","2015 Population","2010 Population","2000 Population","1990 Population","1980 Population","1970 Population"])
    values = df[df["Country/Territory"] == country].values.tolist()[0]
    return dict(zip(df,values))


def percentage_population(path):
    data = pd.read_csv(path)
    values = data.loc[:,"World Population Percentage"].values.tolist()
    countries = data.loc[:,"Country/Territory"].values.tolist()
    return dict(zip(countries,values))

def read_data_from_csv(op, country = "Colombia", path = "data.csv"):
    if op == 1:
        return search_by_country(country, path)
    elif op == 2:
        return percentage_population(path)




if __name__ == "__main__":
    print(read_data_from_csv())
