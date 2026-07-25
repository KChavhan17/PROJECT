#Currency conversion for international client billing
# 1. Take inputs for the INR billing amount and USD Price
inr = float(input("Enter amount in INR: "))
usd_val = float(input("Enter value of 1 USD in INR: "))

# 2. Convert to USD by dividing the total INR by the single dollar value
usd = inr / usd_val

# 3. Calculate the 2% processing fee based on the converted USD amount
fee = usd * 0.02

# 4. Calculate final amount by adding usd and fee amount
total = usd + fee

# 5. Printing amount to pay in USD
print(f"Base USD Amount     : {usd:.2f}")
print(f"Processing Fee (2%) : {fee:.2f}")
print(f"Total Bill in USD   : {total:.2f}")