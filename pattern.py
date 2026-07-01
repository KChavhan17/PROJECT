#
# 1. Store Employee Details
employee_name = "Rahul Sharma"
employee_id = 10123
department = "Software Development"
date = "20 May 2025"
month = "May 2025"

# 2. Store Salary Components
basic_salary = 50000.0
hra = 15000.0
da = 10000.0
tax = 7500.0

# 3. Calculations
gross_salary = basic_salary + hra + da
net_salary = gross_salary - tax

# 4. Display the Salary Slip
print("-" * 50)
print("             ABC SOLUTIONS PVT. LTD.")
print("               Employee Salary Slip")
print("-" * 50)
print(f"Employee Name : {employee_name:<20} Date  : {date}")
print(f"Employee ID   : {employee_id:<20} Month : {month}")
print(f"Department    : {department:<20}")
print("-" * 50)
print(f"{'SALARY DETAILS':<35} {'AMOUNT (INR)':>12}")
print("-" * 50)
print(f"{'Basic Salary':<35} {basic_salary:>12,.2f}")
print(f"{'HRA':<35} {hra:>12,.2f}")
print(f"{'DA':<35} {da:>12,.2f}")
print(f"{'Gross Salary (Basic + HRA + DA)':<35} {gross_salary:>12,.2f}")
print(f"{'Tax':<35} {tax:>12,.2f}")
print("-" * 50)
print(f"{'Net Salary (Gross Salary - Tax)':<35} {net_salary:>12,.2f}")
print("-" * 50)
print("       Thank you for your hard work and dedication!")