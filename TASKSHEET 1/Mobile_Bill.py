#Generating Mobile Bill
mobile_name=input("Enter Mobile Name: ")
mobile_price=float(input("Enter Mobile Price: "))
quantity=int(input("Enter Number of Mobiles:" ))
total_price=mobile_price*quantity
print("----------Mobile Bill---------")
print(f"Mobile Name: {mobile_name}")
print(f"Mobile Price: {mobile_price}")
print(f"Quantity: {quantity}")
print(f"Total Price: {total_price}")