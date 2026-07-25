#Employee Eligibility for Retirement
# Retirement Check Program
# Take employee details as input
name = input("Enter the employee's name: ")
age = int(input("Enter the employee's age: "))
print(f"Employee Name: {name}")
print(f"Employee Age: {age}")

# Check retirement eligibility based on age
if age >= 58:
    print("Eligible for Retirement Benefits")
elif age >= 18:
    print("Eligible for Provident Fund Enrollment")
else:
    print("Not Eligible for Retirement or Provident Fund Enrollment")