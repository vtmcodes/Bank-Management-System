import json

DB_FILE = "storage.json"

def load_data():
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("ERROR! storage.json not found / renamed. ")
        print("Please restore the file before running the ATM system. ")
        return None

def save_data(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)