def quick_sort1(l):
    if len(l) < 2:
        return l
    else:
        pivot = l[0]  # 设定基数
        less_than_pivot = [x for x in l if x < pivot]
        more_than_pivot = [y for y in l if y > pivot]
        return quick_sort1(less_than_pivot) + [pivot] + quick_sort1(more_than_pivot)
def fun(l, start, end):
    if start < end:
        i = start
        j = end
        temp = l[i]
        while i < j:
            while (i < j) and l[j] >= temp:
                j = j - 1
            l[i], l[j] = l[j], l[i]
            while (i < j) and l[i] <= temp:
                i = i + 1
            l[j], l[i] = l[i], l[j]
        l[i] = temp
        fun(l, start, i - 1)
        fun(l, j + 1, end)
    return l
L = [5, 9, 1, 11, 6, 7, 2, 4]
print(fun(L,0,len(L)-1))
