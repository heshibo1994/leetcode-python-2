# n = 2
# k = 2#次数
# l = [4,6]

n, k = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]



minimum = 0
l.sort()
for i, v in enumerate(l):
    if v != 0:
        minimum = v
        index = i
        break
while k > 0:
    print(minimum)
    minimum = l[index+1]-l[index]
    k = k-1

fun(2,2,[4,6])
