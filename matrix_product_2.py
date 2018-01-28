import numpy as np

a_col = int(input("A Row:: "))
a_row = int(input("A Column:: "))

b_col = int(input("B Row:: "))
b_row = int(input("B Column:: "))

if(a_row != b_col):
    print("ERROR")
else:
    #creating the size of the result according to the columns and rows of a and b
    result = [[0 for x in range(b_row)] for y in range(a_col)]
    np.random.seed(1)

    #creating random arrays according to the columns and rows of a and b
    a = np.random.randn(a_col*a_row).reshape(a_col,a_row)
    b = np.random.randn(b_col*b_row).reshape(b_col,b_row)

    for i in range(len(a)): #going through the # of rows
        for j in range(len(b[0])): #going through the # of columns
            temp_add = 0
            for k in range(len(b)):
                temp_add += a[i][k] * b[k][j]
            #adding the multiplied data to the final array
            result[i][j] = temp_add

    #printing calculated result and original correct answers to compare
    print(result)
    print("\n")
    correct_answer = a.dot(b)
    print(correct_answer)
