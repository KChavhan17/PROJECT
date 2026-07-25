#Duplicate-Free Attendee List


print("-"*80)
print("              Duplicate-Free Attendee List           ")
print("-"*80)
print("\n")

# Registration list with a duplicate attendee
attendees = ["Alice", "Bob", "Charlie", "Bob", "Diana"]
print("Original list:", attendees)
print("\n")


# Remove the duplicate entry
attendees.remove("Bob")
print("After removing duplicate:", attendees)
print("\n")


# Archive at year-end by resetting the list
attendees.clear()
print("After archiving (cleared):", attendees)