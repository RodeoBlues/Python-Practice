A = [[3,4,5],[6,7,8],[9,10,11]]

B = [[2,4,8],[9,7,8],[6,5,10]]

length = 3

ans = [[0,0,0], [0,0,0],[0,0,0]]


for i in range(length):
    for j in range(length):
        add = 0
        for k in range(length):
            add += A[i][k] * B[k][j]
        ans[i][j] = add

print(ans)
