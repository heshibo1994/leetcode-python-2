# 实现一个函数，把字符串中的每个空格替换成%20，
# 输入  we are happy
# 输出  we%20are%20happy
s = "we are happy"
def func(s):
    s = list(s)
    p1 = len(s)
    p2 = len(s)+s.count(" ")*2
    ans = [" "]* p2
    while p1 != 0:
        if s[p1-1] == " ":
            ans[p2-1] = '0'
            ans[p2-2] = '2'
            ans[p2-3] = '%'
            p2 = p2 - 3
        else:
            ans[p2-1] = s[p1-1]
            p2 = p2 - 1
        p1 = p1 - 1
    return "".join(ans)
print(func(s))





