n = 1024-int(input())+1
dp = [0]*n
dp[0] = 0
dp[1] = 1
for i in range(2,n):
    if i<4:
        dp[i] = dp[i-1]+1
    if 4<=i<16:
        dp[i] = min(dp[i - 1],dp[i-4]) + 1
    if 16<=i<64:
        dp[i] = min(dp[i - 1], dp[i - 4],dp[i-16]) + 1
    if i>=64:
        dp[i] = min(dp[i - 1], dp[i - 4], dp[i - 16],dp[i-64]) + 1
print(dp[-1])
