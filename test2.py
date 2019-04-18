ans = 0
for i in range(1,866278171,2):
    print(i)
    for j in str(i):
        if j =="3":
            ans=ans+1
    print(i,ans)