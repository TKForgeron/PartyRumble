import json


def load_json(file_path):
    with open(file_path, encoding="utf-8") as file:
        # with open(file_path, "r") as file:
        data = json.load(file)

    return data
