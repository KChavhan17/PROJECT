#Monthly Revenue Report

Monthly_Revenue = [10000, 15000, 12000, 18000, 20000, 25000, 30000, 28000, 35000, 40000, 45000, 50000]
print("Monthly Revenue Report:", Monthly_Revenue)
print("\n")

first_quarter_revenue = (Monthly_Revenue[0:3])
print("Total revenue for the first quarter (Jan-Mar):", first_quarter_revenue)
print("\n")

second_quarter_revenue = (Monthly_Revenue[9:12])
print("Total revenue for the second quarter (Apr-Jun):", second_quarter_revenue)
print("\n")

peak_revenue = first_quarter_revenue+second_quarter_revenue
print("Peak revenue:", peak_revenue)
print("\n")


