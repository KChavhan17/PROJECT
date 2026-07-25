#Sum of entered digits
#n = 12345
n=int(input("Enter n value"))
sum = 0

while n > 0:
    sum += n % 10  # extract last digit
    n //= 10       # remove last digit

print(sum)