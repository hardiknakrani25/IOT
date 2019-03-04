str=input('Enter number : ')
total=0
i=0
while i < len(str):
    total=total+int(str[i])
    i=i+1   
print("Sum of Digit is : ",total)