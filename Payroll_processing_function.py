#Payroll processing function

def net_salary_count(name,basic_salary):
    HRA=basic_salary*0.10
    salary=(basic_salary+HRA)
    net_salary=salary-0.05
    emp_netsalary={"name":name,"basic":basic_salary,"net_salary":net_salary}
    return emp_netsalary

emp_count=int(input("Enter number of employees : "))
emp_salary_d=[]
for i in range(emp_count):
    empname=input("Enter employee name : ")
    basic=int(input("Enter employee basic salary :\n "))
    emp_netsalary=net_salary_count(empname,basic)
    emp_salary_d.append(emp_netsalary)
    
for i in emp_salary_d:
    print("    ---Payroll---")
    print(f"Employee name : {i['name']}")
    print(f"Employee basic salary : {i['basic']}")
    print(f"Employee net salary : {i['net_salary']}")
    print("-" * 30)
