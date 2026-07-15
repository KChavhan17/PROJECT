#Meeting Room Booking Logger

confirm_room=int(input("Enter number of confirm  rooms for booking:"))
room_booked=[]

for i in range(confirm_room):
    room_name=input("Enter room name:")
    start_time=input("Enter meeting start time:")
    end_time=input("Enter meeting end time:")
    room_booked.append([room_name,start_time,end_time])

room_booked=tuple(room_booked)
print("---Confirmed Room Booklist---")   
for booked in room_booked:
    print(f"Room name:{room_name}\nStart_time:{start_time}\nEnd time:{end_time}") 