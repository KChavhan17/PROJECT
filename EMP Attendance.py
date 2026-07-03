#Employee Attendance Management System

print("\n                 Employee Attendance Report          ")
print("-"*70)   

total_working_days=30
emp_name=input("Enter Employee Name: ")
attendance_days=int(input("Enter Number of Days Present: "))

attendance_percentage=(attendance_days/total_working_days)*100
print("\n")

print(f"\n{emp_name}'s Attendance Percentage: {attendance_percentage:.2f}%")

print("\nEmployee Attendance Report")
print("-"*70)   
print(f"\n{'Employee Name                 :'} {emp_name}")
print(f"{'Total Working Days            :'} {total_working_days}")  
print(f"{'Days Present                  :'} {attendance_days}")
print(f"{'Attendance Percentage         :'} {attendance_percentage:.2f}%\n")

if attendance_percentage>=95:
    print("Employee is eligible for a Perfect Attendance Bonus.")
elif attendance_percentage < 95 and attendance_percentage >= 60:
    print("Status:Good Attendance.Normal Salary.")
else:
    print("Cutt off in salary")