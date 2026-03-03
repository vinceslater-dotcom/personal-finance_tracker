import json
import os

from budget import set_budget, show_budget_status

DATA_FILE = "data.json"


def load_data():
    """
    Load financial data from data.json.
    If the file does not exist, return a default structure.
    """
    if not os.path.exists(DATA_FILE):
        return {
            "income": 0,
            "expenses": [],
            "budgets": {}
        }

    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            # If the JSON file is corrupted/empty, reset to default structure
            return {
                "income": 0,
                "expenses": [],
                "budgets": {}
            }


def save_data(data):
    """
    Save financial data into data.json.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ---------------------------
# Income Tracker
# ---------------------------
def add_income(data):
    """
    Add monthly income entered by the user and save it.
    """
    try:
        amount = float(input("Enter monthly income: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return data

    # Add the income to the current value
    data["income"] = float(data.get("income", 0)) + amount

    print("Income added successfully!")
    return data


# ---------------------------
# Main CLI
# ---------------------------
def main():
    """
    Simple CLI menu to manage income, budgets, and display budget status.
    """
    data = load_data()

    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Add income")
        print("2. Set budget (by category)")
        print("3. Show budget status")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            data = add_income(data)
            save_data(data)

        elif choice == "2":
            data = set_budget(data)
            save_data(data)

        elif choice == "3":
            show_budget_status(data)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()