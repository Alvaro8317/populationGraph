import pandas as pd
def read_data_from_csv(path):
    data = pd.read_csv(path)
    # print(data) # Trae las primeras 5 filas y las últimas 5 filas
    # print(data.head(10)) # Trae las primeras 10 filas
    # print(data.tail(10)) # Trae las últimas 10 filas
    # print(data.dtypes) # Trae el como está manejando cada una de las columnas
    df = pd.DataFrame(data, columns=["Continent", "2022 Population","2020 Population","2015 Population","2010 Population","2000 Population","1990 Population","1980 Population","1970 Population"])
    print(df)


if __name__ == "__main__":
    read_data_from_csv("data.csv")
