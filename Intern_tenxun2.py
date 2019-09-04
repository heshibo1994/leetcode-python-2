# 1
# 4
# 4 4 4 3
k = int(input())
a = []
for i in range(k):
    temp = []
    temp.append(int(input()))
    temp.append([int(i) for i in input().split(" ")])
    a.append(temp)

def fun(l):
    a = {}
    for i in l:
        a[i] = a.get(i, 0)+1
    ans =list( a.values())
    temp = []
    num_1 = 0
    for i in ans:
        if i != 1:
            temp.append(i)
        else:
            num_1 +=1
    # num_1 =1
    # temp = [2,3,4,5,6,7,8]
    temp.sort(reverse=True)
    while (len(temp)!=1):
        if len(temp)%2==1:
            temp = [temp[i]-temp[i+1] for i in range(len(temp)//2)]+[temp[-1]]
        else:
            temp = [temp[i] - temp[i + 1] for i in range(len(temp) // 2)]
        temp.sort(reverse=True)
        if sum(temp)<=num_1:
            return "YES"
    return "NO"


for i in range(k):
    print(fun(a[i][1]))

