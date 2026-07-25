#
class Employee:
    def display_info(self):
        print(f"[{self.emp_id}] {self.name} - {self.department}")

emp1=Employee()
emp1.emp_id="169"
emp1.name="Rihan"
emp1.department="HR"

emp2=Employee()
emp2.emp_id="17"
emp2.name="Ria"
emp2.department="sales"

emp1.display_info()
emp2.display_info()