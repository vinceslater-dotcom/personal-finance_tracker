import json
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"incomes": [], "expenses": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)



def calculate_total_income(data):
    return sum(item["amount"] for item in data["incomes"])

def calculate_total_expenses(data):
    return sum(item["amount"] for item in data["expenses"])

def calculate_savings(data):
    total_income = calculate_total_income(data)
    total_expenses = calculate_total_expenses(data)
    return total_income - total_expenses

def show_summary():
    data = load_data()

    total_income = calculate_total_income(data)
    total_expenses = calculate_total_expenses(data)
    savings = calculate_savings(data)

    print("\n--- Résumé financier ---")
    print(f"Revenus : {total_income:.2f} €")
    print(f"Dépenses : {total_expenses:.2f} €")
    print(f"Économies du mois : {savings:.2f} €")

    if savings < 0:
        print("⚠️ Attention : vous dépensez plus que ce que vous gagnez !")
    else:
        print("🎉 Bravo : vous êtes en positif ce mois-ci.")