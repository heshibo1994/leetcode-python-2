#  将n长的绳子剪成m段，求乘积的最大值
def fun(l):
    dp = [0,1,2,3]
    for i in range(4,l+1):
        temp = 0
        for j in range(1,i):
            if dp[j]*dp[i-j]>temp:
                temp = dp[j]*dp[i-j]
        dp.append(temp)
    return dp
print(fun(8))