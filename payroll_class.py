#Payroll  calculator class

class Payroll:
    def calculate_net_salary(self):
        hra=0.40*self.basic_salary
        da=0.10*self.basic_salary
        deduction=0.05*self.basic_salary
        net_salary=self.basic_salary+hra+da-deduction
        return net_salary

salary=Payroll()
salary.basic_salary=80000
net_salary=salary.calculate_net_salary()
print(f"Net salary:{net_salary}")


