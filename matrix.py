def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("\t", matrix[i][j], end=" ")
        print("\n")


def multi():
    m = int(input("enter first matrix rows : "))
    n = int(input("enter first matrix columns : "))
    p = int(input("enter second matrix rows : "))
    q = int(input("enter second matrix columns : "))
    if(n != p):
        print("matrice multipilication not possible...")
        exit()

    array1 = [[0 for j in range(0, n)] for i in range(0, m)]
    array2 = [[0 for j in range(0, q)] for i in range(0, p)]
    result = [[0 for j in range(0, q)] for i in range(0, m)]

    print("enter first matrix elements : ")
    for i in range(0, m):
        for j in range(0, n):
            array1[i][j] = int(input("enter element : "))
    print("enter second matrix elements : ")
    for i in range(0, p):
        for j in range(0, q):
            array2[i][j] = int(input("enter element : "))
    print("first matrix")
    print_matrix(array1)
    print("second matrix")
    print_matrix(array2)

    for i in range(0, m):
        for j in range(0, q):
            for k in range(0, n):
                result[i][j] += array1[i][k] * array2[k][j]

    print("multiplication of two matrices : ")
    print_matrix(result)


def add():
    m = int(input("enter rows : "))
    n = int(input("enter columns : "))

    matrix1 = [[0 for j in range(0, n)] for i in range(0, m)]

    matrix2 = [[0 for j in range(0, n)] for i in range(0, m)]
    res_matrix = [[0 for j in range(0, n)]
                  for i in range(0, m)]
    print("enter first matrix elements")
    for i in range(0, m):
        for j in range(0, n):
            matrix1[i][j] = int(input("enter an element : "))
    print("enter second matrix elements ")
    for i in range(0, m):
        for j in range(0, n):
            matrix2[i][j] = int(input("enter an element : "))

    for i in range(0, m):
        for j in range(0, n):
            res_matrix[i][j] = matrix1[i][j]+matrix2[i][j]

    print(" matrix 1")
    print_matrix(matrix1)
    print(" matrix 2")
    print_matrix(matrix2)

    print("resultant matrix after adding")
    print_matrix(res_matrix)


print("Press 1 for matrix multiplication or Press 2 for matrix Addition")

select = int(input("Enter your choice : "))

if select == 1:
    multi()
elif select == 2:
    add()
else:
    print("Wrong choice!")
