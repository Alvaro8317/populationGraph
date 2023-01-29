import os


def create_folder(path, name_folder="logs"):
    path_to_create = os.path.join(path,name_folder)
    try:
        os.mkdir(path_to_create)
        print("Created successfully!")
    except Exception as err:
        print(f"It has occurred an unexpected error, details: {err}")
        print("Did you started already?")
