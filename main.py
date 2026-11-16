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
                getAllExpenses()

            elif choice == 3:
                searchExpense()
            elif choice == 4:
               





        except Exception as e:
            print(e)
startApp()