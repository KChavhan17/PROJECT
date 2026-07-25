#Duplicate employee id checker

print("\n---Duplicate employee id checker---\n")

employee_id=["py67","py78","py67","py98","py54","py23","py54"]
duplicate_count=len(employee_id)
employee_id=set(employee_id)
unique_count=len(employee_id)
count=duplicate_count-unique_count
print("Duplicate counts:",count)

