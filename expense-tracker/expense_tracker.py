import csv

class ExpenseTracker:
    def __init__(self, file_name):
        # Initialize ExpenseTracker object
        self.file_name = file_name
        self.expenses = []
        self.load_expenses()  # Load existing expenses when object is created

    def load_expenses(self):
        # Load expenses from CSV file into memory
        try:
            with open(self.file_name, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert 'amount' field to float and add each row as a dictionary to 'expenses' list
                    self.expenses.append({'category': row['category'], 'amount': float(row['amount'])})
        except FileNotFoundError:
            print("Expense file not found. Starting with an empty expense list.")

    def save_expenses(self):
        # Save expenses from memory to CSV file
        with open(self.file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['category', 'amount'])
            writer.writeheader()  # Write CSV header
            for expense in self.expenses:
                writer.writerow(expense)  # Write each expense as a row in CSV file

    def add_expense(self, category, amount):
        # Add a new expense to 'expenses' list and save to CSV file
        self.expenses.append({'category': category, 'amount': amount})
        self.save_expenses()

    def total_expenses(self):
        # Calculate total expenses by summing up amounts of all expenses
        total = sum(expense['amount'] for expense in self.expenses)
        return total

    def expenses_by_category(self):
        # Calculate total expenses for each category
        expenses_by_cat = {}
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            if category in expenses_by_cat:
                expenses_by_cat[category] += amount
            else:
                expenses_by_cat[category] = amount
        return expenses_by_cat

    def view_expenses(self):
        # Display all expenses
        for expense in self.expenses:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}")

    def close(self):
        pass  # No need to close anything in this case

def main():
    # Main function to run the expense tracker
    file_name = "expenses.csv"
    tracker = ExpenseTracker(file_name)  # Initialize ExpenseTracker object

    while True:
        # Display menu options
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Add a new expense
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(category, amount)
            print("Expense added successfully!")
        
        elif choice == '2':
            # View all expenses
            print("\nAll Expenses:")
            tracker.view_expenses()
        
        elif choice == '3':
            # View total expenses
            print("\nTotal Expenses:", tracker.total_expenses())
        
        elif choice == '4':
            # View expenses by category
            print("\nExpenses by Category:")
            expenses_by_cat = tracker.expenses_by_category()
            for category, amount in expenses_by_cat.items():
                print(f"{category}: {amount}")
        
        elif choice == '5':
            # Exit the program
            print("Exiting...")
            tracker.save_expenses()  # Save expenses to file before exiting
            break
        
        else:
            # Invalid choice
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
