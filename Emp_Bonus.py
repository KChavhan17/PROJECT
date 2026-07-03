#Employee Bonus Eligibility
years_of_experience=int(input("Enter Years of Experience: "))
performance_rating=float(input("Enter Performance Rating(1-10) : "))

if years_of_experience>2 and performance_rating>=8:
    print("Employee is eligible for a Bonus.")
else:
    print("Employee is not eligible for a Bonus.")