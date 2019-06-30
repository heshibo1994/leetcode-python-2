# 在一个长度为n的数组里的所有数字都在0到n-1的范围内，驻足中某些数字是重复的，但不知道有几个数字重复了们也不不知道每个数字重复的次数
# 找出数组中任意一个重复的数字

l = [2, 3, 1, 0, 2, 5, 3]



def func(l):
    for i in range(len(l)):
        while l[i] != i:
            if l[i] == l[l[i]]:
                return l[i]
            temp = l[i]
            l[i],l[temp] = l[temp],l[i]

print(func(l))