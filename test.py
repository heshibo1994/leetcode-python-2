n = 10
N = 2 * n + 10
l = [[0 for i in range(N)] for j in range(n-2)]
for i in range(n-2):
    if i == 0:
        for j in range(N):
            if j != n - 3 and j != n + 12:
                l[0][j] = " "
            else:
                l[0][j] ="*"
    elif i==1:
        for j in range(N):
            if j != n - 4 and j != n - 3 and j != n - 2 and j != n + 11 and j != n + 12 and j != n + 13:
                l[1][j] = " "
            else:
                l[1][j] ="*"
    else:
        for j in range(N):
            if j != n - i-3 and j != n - i-2 and j != i+6  and j != i+7  and j != i + 18  and j != i + 19 and j !=i + 21  and j != i + 22:
                l[i][j] = " "
            else:
                l[i][j] = "*"
for j in l:
    print(j)
