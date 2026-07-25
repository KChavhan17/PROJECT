# INPUTS TO PROVIDE:
# Manager Name: Alice
# Department: IT
# Tasks: Task 07, Task 08, Task 09, Task 10, Task 11
# Skills: Function, Loop, Tuple, Set, Dictionary
# Hours: (Enter a number for each task, e.g., 4)

# 1. Input basic details
manager = input("Manager Name: ")
dept = input("Department: ")
manager_info = (manager, dept)  # Tuple

# 2. Input tasks and skills
tasks_input = input("Tasks (comma-separated): ")
tasks = tasks_input.split(",")  # List

skills_input = input("Skills (comma-separated): ")
skills = set(skills_input.split(","))  # Set

# 3. Get hours for each task
hours_dict = {}  # Dictionary
total_hours = 0

for t in tasks:  # Loop
    t = t.strip()
    hours = float(input("Hours for " + t + ": "))
    hours_dict[t] = hours
    total_hours = total_hours + hours

# 4. Print Report
print("\n--- REPORT ---")
print("Manager/Dept:", manager_info)
print("Tasks:", tasks)
print("Skills:", skills)
print("Total Hours:", total_hours)

# 5. Check Status
if total_hours >= 20:  # Conditional Statement
    print("Status: On Track")
else:
    print("Status: Needs Catch-up")