#Department class with  e   Employee objects
class Employee:
    pass

class Department:
    dept_name=" "
    employees=[]

    def list_employees(self):
        print(f"Employees in {self.dept_name} Department:")
        for emp in self.employees:
            print(f"-{emp.name}")

dept=Department()
dept.dept_name="IT"
dept.employees=[]

e1=Employee()
e1.name="Rihan"

e2=Employee()
e2.name="Samad"

e3=Employee()
e3.name="Aditya"

dept.employees.append(e1)
dept.employees.append(e2)
dept.employees.append(e3)
dept.list_employees()