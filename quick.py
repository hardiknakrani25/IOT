def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1], x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0], x[i] = x[i], x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part


alist = list()
no = int(input("Enter total no : "))
i = 0

while i < no:
    alist.append(int(input('no : ')))
    i = i+1
print("Numbers are : ", alist)
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Sorted numbers are : ", quicksort(alist))
