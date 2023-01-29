import csv


def read_csv(path):
    with open(path, "r", encoding="utf-8") as csvfile:
        # Delimitador es lo que separa las columnas
        # Reader es un iterable, es decir, la primera fila son las columnas
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = list(zip(header, row))
            # print(iterable)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data


if __name__ == "__main__":
    result = read_csv("final_project\data.csv")