import json
from functools import reduce
from datetime import datetime
#--------------------------------------------------------------
def load_expanses(filename="expanses.json"):
 try:
    with open(filename, "r") as f:
     return json.load(f)
 except FileNotFoundError:
     return []

def save_expanses(expenses,filename="expanses.json"):
    with open(filename, "w") as f:
        json.dump(expenses, f, indent=4)

#------------------------------------------------------------------------

def add_expense(expenses):
     date = input("Enter date (YYYY-MM-DD): ")
     category = input("Enter category (food,travel,shopping....): ")
     amount = float(input("Enter amount ($): "))

     expense = {
         "date": date,
         "category": category,
         "amount": amount,
     }
     expenses.append(expense)
     save_expanses(expenses)
     print(" expenses saved successfully")


#-----------------------------------------------------------------------

def show_report(expenses):

    print("---all expenses---")
    for exp in expenses:
        print(f"{exp['date']}| {exp['amount']}| ${exp['category']}")

    total = reduce(lambda acc,x: acc+x["ammount"], expenses, 0)
    print(f"Total: {total}")

    month = input(" Enter month (YYYY-MM) to se report,or press enter the skip")
    if month:
        monthly_expenses = list(filter(lambda x:x["date"].startswith(month), expenses))
        monthly_expenses = reduce(lambda acc,x: acc+x["amount"], monthly_expenses, 0)
        print(f"Monthly expenses: ${monthly_expenses}")

#-----------------------------------------------------------------------------

def main():
    expanses = load_expanses()
    while True:
        print("\n=====Expense tracker=====")
        print("1. Add an expense")
        print("2. show report")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense(expanses)
        elif choice == "2":
            show_report(expanses)
        elif choice == "3":
            print("---------Exiting----------")
        else:
            print("Invalid choice")


#--------run app-----------

main()



