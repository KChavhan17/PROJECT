#Overtime Salary Calculator

print("\n                    Overtime Salary Calculator          ")
print("-"*70)

working_hours=8
hours_worked=float(input("Enter Total Hours Worked: "))

Regular_pay=working_hours*10.00
Overtime_pay=Regular_pay+(hours_worked-8)*15.00
if hours_worked>8:
    print("Employee has worked overtime.")
    print(f"Regular Pay: {Regular_pay:.2f}")
    print(f"Overtime Pay: {Overtime_pay:.2f}")
    print(f"Total Pay: {Regular_pay+Overtime_pay:.2f}")
else:
    print("Employee has not worked overtime.")
    print(f"Regular Pay: {Regular_pay:.2f}")
    

