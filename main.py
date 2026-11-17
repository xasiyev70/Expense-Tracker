from expense import *
from validation import CATAGORIES
from reporsts import *


def showMenu():
    print("="*40)
    print("         EXPENSE TRACKER          ")
    print("="*40)

    print(
        """
    1. Add Expense
    2. Show All Expense
    3. Edit Expense
    4. Delete Expense
    5. Search Expense
    6.Show Total Expense
    7.Show Categories
    8.Export To Csv

    0. Exit
        """)
    print("="*40)


def startApp():
    while True:
        showMenu()
        choice = int(input("seciminizi daxil edin: "))
        try:
            if choice == 1:
                title = input("enter expense title: ")
                amount = input("enter expense amount: ")
                category = input("enter expense category: ")
                
                
                expense=addExpense(title,amount,category)
                print("expence added successfully!")
                print("Expense ID:",expense["id"])

            elif choice == 2:
                expenses = getAllExpenses()
                for i in expenses:
                    print(i)

            elif choice == 3:
                expenseID = input("enter expense id: ")
                title = input("enter new expense title: ")
                amount = input("enter new expense amount: ")
                category = input("enter new expense category: ")
                updateExpense(expenseID, title, amount, category)
            elif choice == 4:
                expenseID = input("enter expense id: ")
                deleteExpense(expenseID)
            elif choice == 5:
                expenseID = input("enter expense id: ")
                searchExpense(expenseID)
            elif choice == 6:
                totalExpenses()
            elif choice == 7:
                for i in CATAGORIES:
                    print(i)
            elif choice == 8:
                exportToCsv()
            elif choice == 9:
                print("exit app")
                break

        except Exception as e:
            print(e)
startApp()