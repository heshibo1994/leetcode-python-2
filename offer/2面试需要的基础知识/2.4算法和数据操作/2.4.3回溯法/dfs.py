#  判断一个二维数组是否存在包含某个字符串的路径
def define(l, row, col, i, j, path, mask):
    if len(path) == 0:
        return True
    if 0 <= i <= row - 1 and 0 <= j <= col - 1 and l[i * col + j] == path[0] and mask[i][j] != 1:
        mask[i][j] = 1  # 这个地方来过了
        copy = path[1:]  # 将字符串向右移，则下次递归将判断下一个字符
        # 递归，看下一个位置和下一个字符是否满足条件，只要有一个满足，则返回真
        return define(l, row, col, i - 1, j, copy, mask) or define(l, row, col, i + 1, j, copy, mask) or \
               define(l, row, col, i, j - 1, copy, mask) or define(l, row, col, i, j + 1, copy, mask)
    return False  # 不满足连通域条件，返回false
def hasPath(l, row, col, path):
    map = "".join([i for item in l for i in item])  # 二维数组转化成字符串
    l = [i for item in l for i in item]
    count = map.count(path[0])  # 计算起点的个数
    t, k = 0, 0  # 计数每一个起始路径
    if count == 0:
        return False
    while k < count:
        mask = [[0] * col for i in range(row)]  # 判断是否重复
        index = map.find(path[0], t)
        i, j = int(index / col), int(index % col)
        t = index + 1  # 确定下一个起点可能的搜多范围
        k = k + 1
        if define(l, row, col, i, j, path, mask):
            return True
    return False
l = [['a', 'b', 't', 'g'], ['c', 'f', 'c', 's'], ['j', 'd', 'e', 'h']]
print(hasPath(l, len(l), len(l[0]),"bfce"))
