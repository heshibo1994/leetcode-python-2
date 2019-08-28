n = 1000
temp1,temp2 = 1,1
key = int(n//2)+1
for i in range(1,key):
    temp1 = temp1*i
for i in range(key,n+1):
    temp2 = temp2*i
print(int(temp2/temp1/key)%100000007 )
