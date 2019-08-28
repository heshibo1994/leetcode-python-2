# 找出旋转数组中的最小值【3,4,5,6,0,1,2,3】   return 1

def myMin(l):
    start = 0
    end = len(l)-1
    while start <= end:
        if start+1 == end:
            break
        mid = (start+end)//2
        if l[mid]>=l[start]:
            start = mid
        else:
            end = mid
    return l[end]
l = [3,4,5,6,0,1,2,3]
print(myMin(l))

