l =  input().split()
n = int(l[0])
l = l[1:]
temp = []
for i in l:
    temp = temp+[i[index:index + 8] for index in range(0, len(i), 8)]
    if len(temp[-1])<8:
        temp[-1] = temp[-1]+"0"*(8-len(temp[-1]))
temp.sort()
for i in range(len(temp)):
    print(temp[i],end=" ")




a = "qwertyuio"
print([a[i:i+4] for i in range(0,len(a),4)])