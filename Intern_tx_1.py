# K,N = [int(i) for i in input().split()]
# n=0
def fun(K,N):
    n=0
    while(K>2 and N>0):
        K = K//2+K%2
        n = n+1
        N = N-1
    n = n+K
    print(n)

fun(15,4)