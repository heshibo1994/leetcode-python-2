# 4
# 10 5
# 1 50
# 10 5
# 10 1
n =int(input())
value = []
for i in range(n):
    value.append([float(i) for i in input().split()])
def fun(value):
    n = len(value)
    dp = [0]*(n+1)
    dp[1] = value[0][0]
    for i in range(2,n+1):
        dp[i] = max(dp[i-2]+value[i-1][1],dp[i-1]+value[i-1][0])
    print(dp[-1])
fun([[10,5],[1,50],[10,5],[10,100]])
