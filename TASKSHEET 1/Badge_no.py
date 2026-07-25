#Badge Number Generator

print("\n                   Employee Badge ID Generator          ")
print("-"*70)
dept_code=input("Enter Department Code:")
joining_year=input("Enter Joining Year:")
emp_id=input("Enter Employee Number:")

badge_number=dept_code+joining_year+emp_id

print(f"Employee Badge ID: {badge_number}")