from helpers import create_folder
from datetime import datetime
import time
import os
import calendar

# def read_csv(path):
#     with open(path, "r", encoding="utf-8") as csvfile:
#         # Delimitador es lo que separa las columnas
#         # Reader es un iterable, es decir, la primera fila son las columnas
#         reader = csv.reader(csvfile, delimiter=',')
#         header = next(reader)
#         data = []
#         for row in reader:
#             iterable = list(zip(header, row))
#             # print(iterable)
#             country_dict = {key: value for key, value in iterable}
#             data.append(country_dict)
#         return data


if __name__ == "__main__":
    while True:
        try:
            dec = int(input(
            """
            Please introduce an option: 
            1. Initialize the application (Recommended for the first start)
            2. Search by country the population
            0. Exit
            """))
            match dec:
                case 1:
                    path = os.path.dirname(__file__)
                    create_folder(path)
                case 0:
                    break
        except ValueError as err:
            try:
                with open("logs\log_error.log", "a", encoding="utf-8") as file:
                    file.write(f"{datetime.fromtimestamp(calendar.timegm(time.gmtime()))}: {err}\n")
            except FileNotFoundError:
                path = os.path.dirname(__file__)
                create_folder(path)
            print("Invalid option, please try again or check the log")
