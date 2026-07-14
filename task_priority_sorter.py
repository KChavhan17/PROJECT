#Task priority sorter

print("---      Task Priority Sorter      ---")

# The PMO task list (using a list of dictionaries for clean data mapping)
tasks = [
    {"name": "Fix production server crash", "priority": 1},
    {"name": "Prepare Q3 milestone report", "priority": 2},
    {"name": "Update documentation typos", "priority": 5},
    {"name": "Review team sprint velocity", "priority": 3},
    {"name": "Organize desk wires", "priority": 4},
    {"name": "Approve critical security patch", "priority": 1}
]

# Loop through the task list
for task in tasks:
    name = task["name"]
    priority = task["priority"]
    
    # Conditional logic to determine urgency label
    if priority == 1:
        label = "Urgent"
    elif 2 <= priority <= 3:
        label = " Normal"
    else:
        label = "Low"
        
    # Printing the result
    print(f"\n[{label}]    {name}     (Priority: {priority})\n")