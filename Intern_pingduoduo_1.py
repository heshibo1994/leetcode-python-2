# A = [int(i) for i in input().split()]
# B = [int(i) for i in input().split()]

A = [1,2,5,9,4]
B = [2,4,5,10]
def fun(A,B):
    for i in range(1,len(A)-1):
        if A[i]<A[i-1]:
            temp = [A[i-1],A[i+1],i]
            break
    if A[-1]<A[-2]:
        temp = [A[-2],1000000000000,len(A)-1]
    B.sort(reverse = True)

    flag = True
    for j in range(len(B)):
         if temp[0]<B[j]<temp[1]:
             A[temp[2]] = B[j]
             flag = False
             break


    if flag:
        print("NO")
    else:
        for i in A:
            print(i,end = " ")
fun(A,B)