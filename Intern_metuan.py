# n = int(input())
# l = []
# for i in range(n):
#     l.append([int(i) for i in input().split()])
#print(l)
n = 3
l =[[1,2,3,2],[2,5,2,3],[1,4,3,4]]
def f(n,l):
    ans = []
    for i in l:
        a = float(str(i[0])+"."+str(i[1]))
        b = float(str(i[2])+"."+str(i[3]))
        t = (max(a,b)
        if t>=1.0:
            ans = ans+[a,b]
            ans = ans+[(a+b)/n for n in range(int(t),1,-1)]
        else:
            ans = ans + [a, b]
            ans = ans + [(a + b) / n for n in range(int(10*t), 1, -1)]

    print(len(set(ans)))


f(n,l)
int(0.2)

print(abs(2.5-2.3))