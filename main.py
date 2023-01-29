from helpers import create_folder, read_data, create_graph
from datetime import datetime, date
import time
import os
import calendar
import json


def write_log(details):
    with open("logs\log_error.log", "a", encoding="utf-8") as file:
        file.write(
            f"{datetime.fromtimestamp(calendar.timegm(time.gmtime()))}: {details}\n")


def write_data(details, country):
    data = json.dumps(details, indent=4)
    with open(f"data\{date.today()} - {country}.json", "a", encoding="utf-8") as file:
        file.write(
            f"{data}\n")


def ask_graph(result):
    print(result)
    form = input(
        "Do you want a pie or a bar graph? Please write bar or pie\n").lower()
    if form in ["bar", "pie"]:
        create_graph(result, form)
    else:
        print("Invalid option")


if __name__ == "__main__":
    path = os.path.dirname(__file__)
    while True:
        try:
            dec = int(input(
                """
            Please introduce an option: 
            1. Initialize the application (Recommended for the first start)
            2. Search by country the population
            3. Make a chart with the percentage of the population by country
            0. Exit
            """))
            match dec:
                case 1:
                    create_folder(path)
                case 2:
                    country = input(
                        "Please introduce the name of a country: ").title()
                    print(country)
                    try:
                        result = read_data(1, country)
                        try:
                            write_data(result, country)
                            print(
                                f"Information saved successfully in the folder data")
                            graph = input(
                                "Do you want to graph the data? Please write Yes or No\n").lower()
                            match graph:
                                case "yes":
                                    ask_graph(result)
                                case "no":
                                    pass
                        except Exception as error:
                            write_log(error)
                            print("Unexpected error, check the log")
                    except IndexError as err:
                        write_log(err)
                        print("Invalid country, check the log")
                case 3:
                    data = read_data(2)
                    print(data)
                    ask_graph(data)
                case 0:
                    break
                case _:
                    print("Invalid option")
        except ValueError as err:
            try:
                write_log(err)
                print("Invalid option, please try again or check the log")
            except Exception as err:
                print(
                    f"Unexpected error, did you try to use the first option before? Details of the error: {err}")
