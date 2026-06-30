correct_PIN="1234"
attempt=0
while attempt<3:
    pin=input("Enter Your PIN:")
    if pin==correct_PIN:
        print("PIN is correct.Access Granted...!!!")
        break
    else:
        attempt+=1
        print("Wrong PIN.")
if attempt==3:
    print("Account Blocked!")
