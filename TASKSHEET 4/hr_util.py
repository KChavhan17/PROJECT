def generate_emp_id(dept_code, number):
    return f"{dept_code.upper()}-{number:03d}"

def is_eligible_for_bonus(years, rating):
    if years >= 2 and rating >= 4.0:
        return "Eligible"
    else:
        return "Not Eligible"

def calculate_attendance_percent(present_days, total_days):
    if total_days == 0:
        return 0.0
    return (present_days / total_days) * 100