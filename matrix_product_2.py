import numpy as np

#input variables
a_col = 0
a_row = 0

b_col = 0
b_row = 0

INPUT = []

#input function
def inputF(): #Insert the input variables
    inputF.a_col = int(input("A Row:: "))
    inputF.a_row  = int(input("A Column:: "))

    inputF.b_col = int(input("B Row:: "))
    inputF.b_row = int(input("B Column:: "))
    if(inputF.a_row != inputF.b_col):
        print("ERROR. Can't calculate the product of two matrices with given dimension. Please try again.")
        return 1


while(inputF() == 1):
    inputF() #calls the input function again


#insert the input data to the original variables
a_col = inputF.a_col
a_row = inputF.a_row

b_col = inputF.b_col
b_row = inputF.b_row

#creating random arrays according to the columns and rows of a and b
np.random.seed(1)
a = np.random.randn(a_col*a_row).reshape(a_col, a_row)
b = np.random.randn(b_col*b_row).reshape(b_col, b_row)
correct_result = a.dot(b)

#creating the size of the result according to the columns and rows of a and b
result = [[0 for x in range(b_row)] for y in range(a_col)]

#a function that multiplies two given matrices
def product(A,B,C):
    for i in range(len(A)): #going through the # of rows
        for j in range(len(B[0])): #going through the # of columns
            temp_add = 0
            for k in range(len(B)):
                temp_add += A[i][k] * B[k][j]
            #adding the multiplied data to the final array
            C[i][j] = temp_add
    return C
product(a, b, result)
print(result)
