#Employee Directory Builder

def print_employee_name(emp):
    i=1

    print("---Employee names---")
    for empname in emp:
        print(i,":",empname)
        i+=1

emp=["Keerti","Rakshita","Rihan","Aditya","Abdul","Samad"]
print_employee_name(emp)     