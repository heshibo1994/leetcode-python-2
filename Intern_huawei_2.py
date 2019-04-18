# l = input()
# length = len(l)
# i = 0
# temp = ""
# ans = ""
# for i in range(len(l)):
l="3(2(sd)3(ert)A)4(BCV)"


zuo =[]
you = []
num =[]
temp = ""
j = 0
ans = ""
for i in range(len(l)):
    if l[i].isdigit():
        temp = temp + l[i]
    elif l[i] =="(":
        zuo.append(i)
        num.append(temp)
        temp = ""
    elif l[i] ==")":
        you.append(i)
        ans = ans+(l[zuo[-1]+1:you[-1]])*(int(num[-1])-1)
    else:
        ans = ans+l[i]
print(ans)
print(num)

