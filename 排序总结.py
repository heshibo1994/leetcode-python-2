import time
import random


def straight_insertion_sort(l):  # 插入排序
    for i in range(len(l)):
        j = i - 1
        key = l[i]
        while j >= 0:
            if key < l[j]:
                l[j], l[j + 1] = key, l[j]
            j = j - 1
    print("直接插入排序：", l)

def shell_sort(l):  # 希尔排序
    n = len(l)
    h = 1
    while h < n / 3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and l[j] < l[j - h]:
                l[j], l[j - h] = l[j - h], l[j]
                j -= h
        h = h // 3
    print("希尔排序：", l)

def simple_selection_sort(l):  # 简单选择排序
    for i in range(len(l)):
        index = l.index(min(l[i:]))
        l[index], l[i] = l[i], l[index]
    print("简单选择排序", l)

def bubble_sort(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    print(l)

def quick_sort(l,left,right):
    if left<right:
        key = l[left]
        i,j = left,right
        while i < j:
            while (i<j) and l[j]>=key:
                j = j-1
            l[i],l[j] = l[j],l[i]
            while(i<j) and l[i]<=key:
                i = i+1
            l[j],l[i] = l[i],l[j]
        quick_sort(l,left,i-1)
        quick_sort(l,j+1,right)
    return l

def merge_sort( li ):
    #不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
    if len(li) == 1:
        return li

    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    ll = merge_sort( left )
    rl = merge_sort( right )

    return merge(ll , rl)

#这里接收两个列表
def merge( left , right ):
    # 从两个有顺序的列表里边依次取数据比较后放入result
    # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
    result = []
    while len(left)>0 and len(right)>0 :
        #为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
        if left[0] <= right[0]:
            result.append( left.pop(0) )
        else:
            result.append( right.pop(0) )
    #while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    result += left
    result += right
    return result
#li2 = merge_sort(li)
#print(li2)


def bucket_sort(l):
    # 选择一个最大的数
    max_num = max(l)
    # 创建一个元素全是0的列表, 当做桶
    bucket = [0]*(max_num+1)
    # 把所有元素放入桶中, 即把对应元素个数加一
    for i in l:
        bucket[i] += 1

    # 存储排序好的元素
    sort_nums = []
    # 取出桶中的元素
    for j in range(len(bucket)):
        if bucket[j] != 0:
            sort_nums +=[j]*bucket[j]

    print( "桶排序：",sort_nums)


# lists =[random.randint(0, 1000) for i in range(10000)]
lists = [49, 38, 65, 97, 76, 13, 27, 48, 55, 4]
t0 = time.time()
# straight_insertion_sort(lists)
# shell_sort(lists)
# simple_selection_sort(lists)
# bubble_sort(lists)
# quick_sort(lists,0,len(lists)-1)
#print(lists)
bucket_sort(lists)

