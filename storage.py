import json


DATA_FILE = "data/expense.json"

def loadExpenses():
    try:
        with open(DATA_FILE,"r",encoding="utf-8") as f:
            expenses = json.load(f)

        return expenses
    except Exception as e:
        print(e)

def saveExpenses(expense):
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(expense,f,indent=4,ensure_ascii=False)
        print("data ugurla saxlanildi..")