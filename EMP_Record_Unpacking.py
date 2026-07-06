#EMP Record Unpacking

print("-"*80)
print("                       Employee Record Unpacking                   ")
print("-"*80)

# Employee data tuple
emp_data = (101, "Keerti", "HR", 60000)

# Unpacking tuple into named variables
emp_id, name, department, salary = emp_data

# Formatted summary
print(f"ID: {emp_id} | Name: {name} | Dept: {department} | Salary: {salary}")