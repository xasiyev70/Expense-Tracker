from exception import invalidExpense

CATAGORIES = [
    "Food",
    "Shopping",
    "Education",
    "Health",
    "Entertaiment",
    "Other"
]

def validateTitle(title):
    title = title.strip()

    if not title:
        invalidExpense("Title cannot be empty!")

    return title


def validateAmount(amount):
    try:
        amount = float(amount)
    except Exception as e:
        print(e)
    if amount <= 0 :
            invalidExpense("amount must be greater than 0!")

    return amount

        