from helpers import create_folder, read_data, create_graph
from datetime import datetime
import time
import os
import calendar


def write_log(details):
    with open("logs\log_error.log", "a", encoding="utf-8") as file:
        file.write(
            f"{datetime.fromtimestamp(calendar.timegm(time.gmtime()))}: {details}\n")


if __name__ == "__main__":
    path = os.path.dirname(__file__)
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
                    create_folder(path)
                case 2:
                    country = input("Please introduce the name of a country: ").capitalize()
                    try:
                        result = read_data(country)
                        print(result)
                        graph = input(
                            "Do you want to graph the data? Please write Yes or No\n").lower()
                        match graph:
                            case "yes":
                                form = input(
                                    "Do you want a pie or a bar graph? Please write bar or pie\n").lower()
                                if form in ["bar", "pie"]:
                                    create_graph(result, form)
                                else:
                                    print("Invalid option")
                            case "no":
                                pass
                    except IndexError as err:
                        write_log(err)
                        print("Invalid country, check the log")
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
