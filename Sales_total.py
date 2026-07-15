#Sales total calculator
sales=[25000,30000,35000,40000,45000,50000,55000]
total=0
i=1
days=len(sales)
print("---Sales Total Calculator---")
for sale in sales:
    total+=sale
    print(f"Day{i}:{sale}")
    i+=1
average=total/days
print("Total sales:",total)
print(f"Average sales:{average:.2f}")
