

def fun(s):
    s = s[::-1]
    temp =s[0]
    ans1= []
    for i in range(1,len(s)):
        temp = s[i]+temp
        if len(temp)%3==0:
            ans1.append(temp)
            temp = ""
    ans1.append("0"*(3-len(s)%3)+s[len(s)-len(s)%3:])
    ans1=ans1[::-1]
    #print(ans1)
    s2 =""
    for i in range(len(ans1)):
        s2 =s2+"0"*(10-len(bin(int(ans1[i]))[2:]))+bin(int(ans1[i]))[2:]
    s2 = str(int(s2))
    #print(s2)
    s2 = s2[::-1]
    temp2 = s2[0]
    ans2 = []
    for i in range(1, len(s2)):
        temp2 = s2[i] + temp2
        if len(temp2) % 5 == 0:
            ans2.append(temp2)
            temp2 = ""
    ans2.append("0" * (5 - len(s2) % 5) + s2[len(s2) - len(s2) % 5:])
    ans2 = ans2[::-1]
    #print(ans2)
    ans3 = []
    for i in range(len(ans2)):
        ans3.append(int(ans2[i],2))
    #print(ans3)
    l1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    l2 = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V"]
    a = dict(zip(l1,l2))
    ans =""
    for i in range(len(ans3)):
        ans =ans+a[ans3[i]]
    print(ans)

n = int(input())
num =[]
while n:
    num.append(input())
    n =n-1
#print(num)

for i in range(len(num)):
    fun(num[i])

