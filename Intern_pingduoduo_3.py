
# MN = [int(i) for i in input().split()]
# M, N= MN[0],MN[1]
#
# m = [int(i) for i in input().split()]
# n = []
# for i in range(N):
#     n.append([int(i) for i in input().split()])
M = 5
N = 4
m = [1, 2, 1, 1, 1]
n =[[1, 2],[2, 3],[3, 4],[3, 5]]
def fun(M,N,m,n):
    b = {}
    for i in range(1,M+1):
        b[i] = m[i-1]
    print(b)
    ans = []
    a = {}
    temp = []
    for i in range(M):
        temp.append([])
    for i in range(len(n)):
        if n[i][0] not in a:
            a[n[i][0]] = 0
            a[n[i][1]] = a[n[i][0]]+1
        else:
            a[n[i][1]] = a[n[i][0]] + 1
    for i in a.keys():
        temp[a[i]].append(i)
    print(temp)
    for i in range(len(temp)):
         if len(temp)!=0:
             if len(temp[i])==1:
                 ans.append(temp[i][0])
             else:
                 temp[i].sort(key = lambda x:b[x])
                 ans +=temp[i]
    for i in ans:
        print(i,end=" ")
fun(M,N,m,n)