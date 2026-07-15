#Employee Bonus Eligibility Function
def bonus_eligible(rating,experience):
    if experience>2 and rating>=8:
        return "Eligible for bonus"
    else:
        return "Not eligible for bonus"

print("Enter Employee Details---")
emp_details=[]
emp_count=int(input("Enter number of employees:"))    
for i in range(emp_count):
    emp_name=input("Enter Employees name:")
    experience=int(input("Enter Employee Experience:"))
    rating=int(input("Enter Employee rating(1-10):"))
    bonus=bonus_eligible(rating,experience)
    emp_details.append([emp_name,experience,rating,bonus])

for emp in emp_details:
        print(f"{emp[0]}:{emp[3]}")