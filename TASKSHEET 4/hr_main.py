import hr_util

# Test 1: Generate ID
emp_id = hr_util.generate_emp_id("HR", 5)
print("Generated ID:", emp_id)

# Test 2: Bonus Eligibility
eligible = hr_util.is_eligible_for_bonus(years=3, rating=4.5)
print("Eligible for Bonus:", eligible)

# Test 3: Attendance Percentage
attendance = hr_util.calculate_attendance_percent(present_days=22, total_days=24)
print(f"Attendance: {attendance:.2f}%")