import pandas as pd
def read_data_from_csv(country = "Colombia", path = "data.csv",):
    data = pd.read_csv(path)
    df = pd.DataFrame(data, columns=["Country/Territory", "2022 Population","2020 Population","2015 Population","2010 Population","2000 Population","1990 Population","1980 Population","1970 Population"])
    values = df[df["Country/Territory"] == country].values.tolist()[0]
    return dict(zip(df,values))



if __name__ == "__main__":
    print(read_data_from_csv())
