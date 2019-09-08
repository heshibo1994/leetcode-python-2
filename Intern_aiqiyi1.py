# print(3/7)
# print(6/35)
# print(1/35)
# print(3/7+6/35+1/35)
def func(r,b):
    k = (r+b)//3 # 最多有几轮
    temp = []
    for i in range(r+b):
        if i%3 == 2:
            temp.append([1,1])
        else:
            temp.append(1)
    print(temp)
    ans1 = r/r+b
    ans2 = (b/r+b)
    for i in range(r+b):
        ans = (b/r+b-i)
    for i in range(k):
        for j in range(r+b):
            temp[j] = (r-j)/(r+b-j)

        if i%3 ==0 :
            temp[i] = r/r+b
            ans.append(1)

    # p = []
    # p.append(r/r+b)
    # for i in range(k):
    #     temp = 1
    #     for j in range(2):
    #         temp *= (b-j)/(r+b-j)
    #     temp *= (b-2)
func(3,4)
