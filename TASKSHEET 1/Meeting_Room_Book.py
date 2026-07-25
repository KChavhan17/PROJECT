#Meeting Room Booking Conflict Checker
# 1. Gather scheduling times for both the existing and the new meeting requests
print("Enter the existing meeting times formate(e.g., 9.00 for 9 AM, 14.30 for 2:30 PM):")
exist_start = float(input("Enter existing meeting start time: "))
exist_end = float(input("Enter existing meeting end time: "))
new_start = float(input("Enter new meeting start time: "))
new_end = float(input("Enter new meeting end time: "))

# 2. Check if the new meeting completely finishes before the existing one begins
no_overlap_before = new_end <= exist_start

# 3. Check if the new meeting starts only after the existing one finishes
no_overlap_after = new_start >= exist_end

# 4. A conflict exists if it does NOT fit completely before or completely after the existing meeting
if not (no_overlap_before or no_overlap_after):
    conflict = "Conflict Detected have to reschedule the meeting"
else:
    conflict = "NO Conflict Detected"

# 5. Print the final boolean evaluation result to display the room availability status
print("Scheduling Conflict Detected:", conflict)