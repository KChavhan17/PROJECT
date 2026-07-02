sn=input("Enter Student Name:") 
si=int(input("Enter Student ID:"))
cn=input("Enter Course Name:")
du=input("Enter Duration:")
e=input("Enter Email:")
mn=int(input("Enter Mobile Number:"))
cf=float(input("Enter Course Fee:"))
rf=float(input("Enter Registration Fee:\n"))

rm=cf-rf

print("\nRegistration Receipt\n")
print("-"*70)

print(f"\n{'Student Name                  :'} {sn}")
print(f"{'Student ID                    :'} {si}")
print(f"{'Course Name                   :'} {cn}")
print(f"{'Duration                      :'} {du}")
print(f"{'Email                         :'} {e}")
print(f"{'Mobile Number                 :'} {mn}")
print(f"{'Course Fee                    :'} {cf}")
print(f"{'Registration Fee              :'} {rf}\n")
print("-"*70)
print(f"\n{'Remaining Fee                :'} {rm}\n")

print("Welcome to Bright Future Institute!")
print("We wish you a great learning journey.")
             
       

