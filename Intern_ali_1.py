n = int(input())
l = []
for i in range(n):
    l.append(float(input()))

def f(n,l):
    ans = 0.0
    a = 100//n
    b = 100%n
    if n%2==0:
        for j in range(a):
            for i in range(0,len(l),2):
                if i==0 and j==0:
                    ans =l[0]
                else:
                    ans = ans+l[i]*(1-ans)
                ans = ans+l[i+1]*(1-ans)
        for k in range(b):
            ans = ans+l[i]*(1-ans)
        print ((str(round(ans, 4)) + "0" * (6 - len(str(round(ans, 4))))))
    if n%2==1:
        s =0
        while s<a:
            for i in range(s%2, len(l), 2):
                if i == 0 and j == 0:
                    ans = l[0]
                else:
                    ans = ans + l[i] * (1 - ans)
                ans = ans + l[i + 1] * (1 - ans)
        for k in range(b):
            ans = ans + l[i] * (1 - ans)
            s = a + 1
        for k in range(b):
            ans = ans + l[i] * (1 - ans)
        print ((str(round(ans, 4))+"0"*(6-len(str(round(ans, 4))))))
f(n,l)