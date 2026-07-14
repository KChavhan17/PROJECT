#Monthly Attendence Tracker

print("\n --- Monthly Attendence Tracker--- \n")
i=1
Present=0
Absent=0
Attendence={}

print("Enter 1 for Present, 0 for Absent")

while i<=30:
    j=int(input(f"{i}: "))
    Attendence[i]=j
    if j==0:
        Absent+=1
    else:
        Present+=1
    i+=1

print("---Employee Attendence---")  
percentage=(Present/30)*100
print("Present:",Present)
print("Absent:",Absent)
print("Percentage:",percentage)

if percentage==100:
    status="Perfect"
elif percentage>75:
    status="Good"
else:
    status="Too low"
print("Status:",status) 




