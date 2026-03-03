class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append({
            "amount": amount,
            "category": category
        })
        print("Dépense ajoutée avec succès.")

    def total_expenses(self):
        return sum(exp["amount"] for exp in self.expenses)

    def expenses_by_category(self):
        categories = {}
        for exp in self.expenses:
            cat = exp["category"]
            categories[cat] = categories.get(cat, 0) + exp["amount"]
        return categories

    def summary(self):
        print("\n------ RÉSUMÉ DES DÉPENSES ------")
        print(f"Total dépenses : {self.total_expenses()} €")

        print("\nPar catégorie :")
        for cat, amount in self.expenses_by_category().items():
            print(f"{cat} : {amount} €")
        print("------------------------------")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Ajouter une dépense")
        print("2. Voir le résumé des dépenses")
        print("3. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            try:
                amount = float(input("Montant de la dépense : "))
                category = input("Catégorie (ex: Nourriture, Loyer, Transport) : ")
                tracker.add_expense(amount, category)
            except ValueError:
                print("Veuillez entrer un montant valide.")

        elif choice == "2":
            tracker.summary()

        elif choice == "3":
            print("Au revoir 👋")
            break

        else:
            print("Option invalide.")


if __name__ == "__main__":
    main()
    