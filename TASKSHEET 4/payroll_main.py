from employee import Employee
import salary_module

# Create Employee 1
e1 = Employee()
e1.name = "Ravi Kumar"
e1.basic_salary = 50000

# Create Employee 2
e2 = Employee()
e2.name = "Anita Sharma"
e2.basic_salary = 60000

# Create Employee 3
e3 = Employee()
e3.name = "Vikram Patel"
e3.basic_salary = 45000

employees = [e1, e2, e3]

print("--- PAYROLL REPORT ---")
for emp in employees:
    net_sal = salary_module.calculate_net_salary(emp.basic_salary)
    print(f"Employee: {emp.name} | Net Salary: ₹{net_sal:.2f}")