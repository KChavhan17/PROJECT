#Task Assignment Queue

print("-"*70)
print("                  Task Assignment Queue                ")
print("-" * 70)
print("\n")

pending_tasks = ["Prepare report", "Attend meeting", "Code review", "report email"]
print("List of pending tasks:", pending_tasks)
print("\n")

popped_task = pending_tasks.pop(0)
print("Popped task:", popped_task)
print("\n")

print("Updated list of pending tasks:", pending_tasks)
print("\n")

client_tasks=["Preparing presentation", "Client call", "Update documentation"]
print("List of client tasks:", client_tasks)
print("\n")

pending_tasks.extend(client_tasks)
print("Updated list of pending tasks:", pending_tasks)
print("\n")