import csv


from expense import getAllExpenses


def totalExpenses():
    expenses = getAllExpenses()
    total = 0
    for i in expenses:
        total += i["amount"]

    print(total)


def exportToCsv():
    expenses = getAllExpenses()

    filePath = "data/expenses.csv"
    
    fieldNames = ["id","title","amount","category","date"]
    
    with open("expenses.csv","w",encoding="utf-8") as f:
        writer = csv.DictWriter(f,fieldnames=fieldNames)
        writer.writeheader()
        writer.writerows(expenses)

    return filePath
        
