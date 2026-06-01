"""
budget.py

Contains all logic related to budget management.
"""

def set_budget(data):
    """
    Define or update a monthly budget for a specific category.
    """

    category = input("Enter category name (e.g., Food, Rent): ").strip()

    if "budgets" not in data:
        data["budgets"] = {}

    amount = float(input(f"Enter monthly budget for '{category}': "))

    data["budgets"][category] = amount

    print(f"Budget successfully set for {category}: {amount}€")

    return data


def show_budget_status(data):
    """
    Display the comparison between budgets and expenses.
    """

    budgets = data.get("budgets", {})
    expenses = data.get("expenses", [])

    if not budgets:
        print("No budgets defined yet.")
        return

    spent_by_category = {}

    for expense in expenses:
        category = expense.get("category", "Other")
        amount = float(expense.get("amount", 0))
        spent_by_category[category] = spent_by_category.get(category, 0) + amount

    print("\n--- Budget Status ---")

    for category, budget in budgets.items():
        spent = spent_by_category.get(category, 0)
        remaining = float(budget) - spent

        print(f"{category} | Budget: {budget}€ | Spent: {spent}€ | Remaining: {remaining}€")

        if remaining < 0:
            print("⚠️ Budget exceeded!")