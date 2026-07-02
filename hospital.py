pn=input("Enter Patient Name:")
age=int(input("Enter Patient Age:"))
gender=input("Enter Patient Gender:")
bg=input("Enter Patient Blood Group:")
w=float(input("Enter Patient Weight:"))
h=float(input("Enter Patient Height:"))
c=float(input("Enter Consultation Fee:"))
rc=float(input("Enter Registration Charge:\n"))

total_Amount_Payable=c+rc
print("\nPatient Information Card\n") 
print("-"*70)
print(f"{'Patient Name        '} {pn}")
print(f"{'Age                 '} {age}")
print(f"{'Blood Group         '} {bg}")
print(f"{'Weight              '} {w}")
print(f"{'Height              '} {h}")
print(f"{'Consultation Fee    '} {c}")
print(f"{'Registration Charge '} {rc}\n")
print("-"*70)
print(f"\n{'Total Amount Payable':<15} {c+rc}\n")
print("Thank you! We wish you good health.")

    
