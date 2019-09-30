a = [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
def fun(l):
    list = []
    while 1:
        for i in range(len(l[0])):
            list.append(l[0].pop(0))
        l.pop(0)

        for j in range(len(l)):
            list.append(l[j].pop(-1))

        for k in range(len(l[0])):
            list.append(l[-1].pop(-1))
        l.pop(-1)

        for ll in range(len(l)):
            list.append(l[-1-ll].pop(0))
        return list


print(fun(a))