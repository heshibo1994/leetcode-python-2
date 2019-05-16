# 累加数是一个字符串，组成它的数字可以形成累加序列。
#
# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
#
# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
#
# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
#
# 示例 1:
#
# 输入: "112358"
# 输出: true
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
#
# 示例 2:
#
# 输入: "199100199"
# 输出: true
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
class Solution:
    def isAdditiveNumber(self, num):
        ans = []
        def f(l):
            if len(l) <= 2:
                return False
            for i in range(2, len(l)):
                if int(l[i]) != int(l[i - 1]) + int(l[i - 2]):
                    return False
            for i in l:
                if i[0] == "0" and i != "0":
                    return False
            return True

        def dfs(k, l):
            if len("".join(l)) == len(num):
                print(l)
                if f(l):
                    ans.append( l[:])
                    return
            temp = ""
            for i in range(k, len(num)):
                if len(ans)==1:
                    return
                temp = temp + num[i]
                l.append(temp)
                dfs(i + 1, l)
                l.pop()

        dfs(0, [])
        if len(ans)==0:
            return []
        return [int(i) for i in ans[0]]
s = Solution()
print(s.isAdditiveNumber("123456579"))
