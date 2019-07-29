#l = [i for i in input().split()]
l = ['CAT', 'A', 'TPC']
l = ["CAT", "TIGER", "RPC"]
def fun(l):

    t1 = []
    for i in l:
        if len(i)==1:
            t1.append(i)

    temp = ""
    d = {}
    for i in  range(len(l)):
        if len(l[i])!=1:
            temp+=l[i][0]+l[i][-1]
        else:
            temp+=l[i]

    for i in temp:
        d[i] = d.get(i,0)+1
    for i in d.keys():
        if i not in t1:
            if d[i]%2!=0:
                return "false"
        else:
            if d[i]<3 or d[i]%2==0:
                return "false"
    return "true"

print(fun(l))