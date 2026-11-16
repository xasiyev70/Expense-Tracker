def expensesNotFound():
    raise LookupError("Expense not found!")

def invalidExpense(massage):
    raise ValueError(massage)