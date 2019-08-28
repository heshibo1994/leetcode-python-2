#  判断某一个数的二进制包含几个1
def fun(c):
    ans = 0
    while c:
        c = c & (c-1)
        ans = ans + 1
    return ans
print(fun(9))

# 判断某一个数是不是2的次方
def fun1(c):
    if (c-1)&c == 0:
        return True
    else:
        return False
print(fun1(64))
