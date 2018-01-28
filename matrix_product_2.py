import numpy as np

a_col = int(input("A Row:: "))
a_row = int(input("A Column:: "))

b_col = int(input("B Row:: "))
b_row = int(input("B Column:: "))

if(a_row != b_col):
    print("ERROR")
else:
    result = [[0 for x in range(b_row)] for y in range(a_col)]
    print(result)
    np.random.seed(1)

    a = np.random.randn(a_col*a_row).reshape(a_col,a_row)
    print(a)
    print("\n")
    b = np.random.randn(b_col*b_row).reshape(b_col,b_row)
    print(b)
    print("\n")


    for i in range(a_col):
        for j in range(b_row):
            temp_add = 0
            for k in range(a_row):
                temp_add += a[i][k] * b[k][j]
            result[i][j] = temp_add
    print(result)
    print("\n")
    correct_answer = a.dot(b)
    print(correct_answer)
