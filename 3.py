import datetime

class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.date} - {self.amount} - {self.category} - {self.description}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, amount, category, description):
        expense = Expense(date, amount, category, description)
        self.expenses.append(expense)

    def list_expenses(self):
        for expense in self.expenses:
            print(expense)

    def calculate_total_expenses(self, time_frame):
        total = 0
        now = datetime.datetime.now()

        if time_frame == "daily":
            start_date = now - datetime.timedelta(days=1)
        elif time_frame == "weekly":
            start_date = now - datetime.timedelta(weeks=1)
        elif time_frame == "monthly":
            start_date = now - datetime.timedelta(days=30)
        else:
            print("Invalid time frame")
            return

        for expense in self.expenses:
            expense_date = datetime.datetime.strptime(expense.date, "%Y-%m-%d")
            if expense_date >= start_date:
                total += expense.amount

        print(f"Total expenses for {time_frame}: {total}")

    def generate_monthly_report(self, month, year):
        report = {}
        for expense in self.expenses:
            expense_date = datetime.datetime.strptime(expense.date, "%Y-%m-%d")
            if expense_date.month == month and expense_date.year == year:
                if expense.category in report:
                    report[expense.category] += expense.amount
                else:
                    report[expense.category] = expense.amount

        print(f"Monthly report for {month}/{year}:")
        for category, total in report.items():
            print(f"{category}: {total}")

    def save_data(self, file_path):
        with open(file_path, 'w') as file:
            for expense in self.expenses:
                file.write(f"{expense.date},{expense.amount},{expense.category},{expense.description}\n")

    def load_data(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                date, amount, category, description = line.strip().split(',')
                self.add_expense(date, float(amount), category, description)

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Calculate total expenses")
        print("4. Generate monthly report")
        print("5. Save data")
        print("6. Load data")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expense(date, amount, category, description)
        elif choice == '2':
            tracker.list_expenses()
        elif choice == '3':
            time_frame = input("Enter time frame (daily, weekly, monthly): ")
            tracker.calculate_total_expenses(time_frame)
        elif choice == '4':
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year: "))
            tracker.generate_monthly_report(month, year)
        elif choice == '5':
            file_path = input("Enter file path to save data: ")
            tracker.save_data(file_path)
        elif choice == '6':
            file_path = input("Enter file path to load data: ")
            tracker.load_data(file_path)
        elif choice == '7':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
