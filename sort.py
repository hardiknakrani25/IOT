num_array = list()
positive_array = list()
negative_array = list()
num = input("Enter how many elements you want:")
print('Enter numbers in array: ')
for i in range(int(num)):
    n = input("num :")
    num_array.append(int(n))
newlist = sorted(num_array)
print('SORTED ARRAY: ', newlist)

for i in range(len(newlist)):
    if newlist[i] >= 0:
        positive_array.append(newlist[i])
    elif newlist[i] < 0:
        negative_array.append(newlist[i])
print('Positive Number : ', positive_array)
print('Negative Number : ', negative_array)
