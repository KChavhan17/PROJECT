# Company  Budget  Allocation   Checker
budget_amount=float(input("Enter your total budget amount:"))
allocated_budget=float(input("Enter your allocated budget amount:"))
department_performance=float(input("Enter your department performance rating(1-10):"))

if budget_amount<=allocated_budget and department_performance>=7:

    print("Your allocated budget is within the total budget amount and " \
    "your department " \
    "performance is good.")

else:

    
    print("Your allocated budget exceeds the total budget amount"
    " and your department performance needs improvement.")
