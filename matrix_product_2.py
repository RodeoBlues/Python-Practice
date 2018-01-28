import numpy as np

a_col = int(input("A Row:: "))
a_row = int(input("A Column:: "))

b_col = int(input("B Row:: "))
b_row = int(input("B Column:: "))


def product(AC, AR, BC, BR):
    if(AR != BC):
        print("ERROR. Can't calculate the product of two matrices with given dimension.")
        return
    else:
        #creating random arrays according to the columns and rows of a and b
        a = np.random.randn(AC*AR).reshape(AC,AR)
        b = np.random.randn(BC*BR).reshape(BC,BR)
        correct_result = a.dot(b)

        #creating the size of the result according to the columns and rows of a and b
        result = [[0 for x in range(BR)] for y in range(AC)]
        np.random.seed(1)

        for i in range(len(a)): #going through the # of rows
            for j in range(len(b[0])): #going through the # of columns
                temp_add = 0
                for k in range(len(b)):
                    temp_add += a[i][k] * b[k][j]
                #adding the multiplied data to the final array
                result[i][j] = temp_add

        print("Correct Answer:: ")
        print( correct_result )
        print("\n")

        print("My Caluclation:")
        print( result )
        print("\n")
        
        return

product(a_col, a_row, b_col, b_row)
