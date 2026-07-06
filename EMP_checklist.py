#Employee Onboarding Checklist
# Initial onboarding checklist for DDI new hires
onboarding_checklist = ["Laptop issued", "ID card created",]
print("📋 Initial Checklist:")
print(onboarding_checklist)
print("-" * 40)

# 1. Using append() to add a new task at the very end
new_task=input("Enter a new task to add to the checklist: ")
onboarding_checklist.append(new_task)
print(" After appending a new task:")
print(onboarding_checklist)
print("-" * 40)

# 2. Using insert() to push an urgent task to position 0 (the absolute front)
urgent_task=input("Enter an urgent task to add to the front of the checklist: ")
onboarding_checklist.insert(0, urgent_task)
print(" After inserting an urgent task at position 0:")
print(onboarding_checklist)