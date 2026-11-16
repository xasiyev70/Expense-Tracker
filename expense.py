import uuid
from datetime import date
from storage import loadExpenses,saveExpenses
from validation import validateTitle,validateCategory,validateAmount
from exception import expensesNotFound



def addExpense(title,amount,category):
    expenses = loadExpenses()

    expense = {
        "id":str(uuid.uuid4())[:8],
        "title":validateTitle(title),
        "amount":validateAmount(amount),
        "category":validateCategory(category),
        "date":date.today().isoformat()
    }

    expenses.append(expense)
    saveExpenses(expenses)

    return expense

def getAllExpenses():
    return loadExpenses()


def searchExpense(expenseId):
    expenses = loadExpenses()
    for i in expenses:
        if i["id"] == expenseId:
            print(i)
        else:
            print(expensesNotFound())

def updateExpense(expenseId,title,amount,category):
    expenses = loadExpenses()
    for i in expenses:
        if i["id"] == expenseId:
            titleN = validateTitle(title)
            amountN = validateAmount(amount)
            categoryN = validateCategory(category)

            i["title"] = titleN
            i["amount"] = amountN
            i["category"] = categoryN

            saveExpenses(expenses)

            print('ugurla deyisildi...')
    return expensesNotFound()


def deleteExpense(expenseId):
    expenses = loadExpenses()
    for i in expenses:
        if i["id"] == expenseId:
            expenses.remove(i)

            saveExpenses(expenses)
            return "ugurla silindi..."
    return expensesNotFound()