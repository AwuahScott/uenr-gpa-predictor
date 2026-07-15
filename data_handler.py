import json
import os

DATA_FILE = "student_records.json"

def load_data():
    """Loads student academic records from a JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

def save_data(data):
    """Saves student academic records to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
