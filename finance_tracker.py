import json
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {
            "income": 0,
            "expenses": [],
            "budgets": {}
        }
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Income Tracker
def add_income(data):
    amount = float(input("Enter monthly income: "))
    data["income"] += amount
    save_data(data)
    print("Income added successfully!")

# execute the def
if __name__ == "__main__":
    data = load_data()
    add_income(data)