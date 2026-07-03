#This is a business report script that generates a summary of financial data for a company. It includes functions to calculate revenue, expenses, and profit margins, as well as to create visualizations of the data. The report can be exported in various formats such as PDF or Excel for easy sharing with stakeholders.

print("\nBusiness Financial Report\n")
print("-"*70)


income=float(input("\nEnter Your Monthly Income:"))
expenses=float(input("Enter  Your Monthly Total Expenses:"))
profit=income-expenses


if income==0:
    print("Company is broke!")
elif income>expenses:
    print(f"\nYour Monthly Profit is: {profit:.2f}")
    print("Congratulations! Your business is profitable.")
elif income<expenses:
    print(f"\nYour Monthly Loss is: {profit:.2f}")
    print("Warning! Your business is operating at a loss.")
else:
    print("\nCompany is not making any profit or loss.")