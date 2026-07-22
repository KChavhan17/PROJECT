#Company-wide class attribute
class Employee:
    company_name="Digital Dreams Institute"
emp1=Employee()
emp1.emp_id="169"
emp1.name="Keerti"


emp2=Employee()
emp2.emp_id="17"
emp2.name="Ria"

print(f"{emp1.name} works at {emp1.company_name}")
print(f"{emp2.name} works at {emp2.company_name}")
