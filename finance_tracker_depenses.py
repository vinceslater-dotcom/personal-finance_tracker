class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append({
            "amount": amount,
            "category": category
        })
        print("Expense added successfully.")

    def total_expenses(self):
        return sum(exp["amount"] for exp in self.expenses)

    def expenses_by_category(self):
        categories = {}
        for exp in self.expenses:
            cat = exp["category"]
            categories[cat] = categories.get(cat, 0) + exp["amount"]
        return categories

    def summary(self):
        print("\n------ EXPENSE SUMMARY ------")
        print(f"Total expenses: {self.total_expenses()} €")

        print("\nBy category:")
        for cat, amount in self.expenses_by_category().items():
            print(f"  {cat}: {amount} €")
        print("------------------------------")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add expense")
        print("2. View expense summary")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Expense amount: "))
                category = input("Category (e.g., Food, Rent, Transport): ")
                tracker.add_expense(amount, category)
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "2":
            tracker.summary()

        elif choice == "3":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
