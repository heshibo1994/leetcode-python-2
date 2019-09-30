# n, m = [int(i) for i in input().split()]
n = 4
m = 2


def fun1(n):
    if n<=1:
        return 1
    return fun1(n-1)*n
def fun(n,m):
    dp = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i == j :
                dp[i][j] = fun1(i+1)
            elif j == 0  :
                dp[i][j] = 1
    for i in range(1,n):
        for j in range(1,min(m,i)):
            dp[i][j] = (j+1)*(dp[i-1][j]+dp[i-1][j-1])

    print(dp[-1][-1])
fun(4,2)

