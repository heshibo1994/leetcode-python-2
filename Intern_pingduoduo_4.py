n = int(input())
s = [int(i) for i in input().split()] # 面积
w = [int(i) for i in input().split()] # 重量

def fun(n,s,w):
    a = {}
    for i in range(n):
        a[s[i]] = w[i]
    b = sorted(a.keys(),reverse=True)
    print(a)
    print(b)

fun(n,s,w)
