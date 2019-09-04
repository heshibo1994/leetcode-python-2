# 3 3 4
l = [int(i) for i in input().split(" ")]
m, n, k = l[0],l[1],l[2]
ans = []
for i in range(m,0,-1):
    for j in range(n,0,-1):
        print(i*j,end = ",")
    print()

