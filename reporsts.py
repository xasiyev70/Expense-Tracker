import csv


from expense import getAllExpenses


def totalExpenses():
    expenses = getAllExpenses()
    total = 0
    for i in expenses:
        total += i["amount"]

        print(total)

def exporToCsv():
    expenses = getAllExpenses()

    filePath = "data/expenses.csv"

    fieldNames = ["id","title","amount","category","date"]
    
    with open("expense.csv","w",encoding="utf-8") as f:
        writer = csv.reader(f,newFile="",FieldNames=fieldNames)
        writer.writeheader()
        writer.writerows(expenses)

    return filePath
        
