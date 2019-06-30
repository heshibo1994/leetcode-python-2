#  编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
#     每行中的整数从左到右按升序排列。
#     每行的第一个整数大于前一行的最后一个整数。

l = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
target = 7
def func (l,target):
    row = 0
    col = len(l[0])-1

    while(row<len(l) and col>=0):
        if l[row][col] <target:
            row +=1
        elif l[row][col] >target:
            col -=1
        else:
            return True
    return False


print(func(l,7))



