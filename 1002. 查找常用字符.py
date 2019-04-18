# 给定仅有小写字母组成的字符串数组
# A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现
# 3
# 次，但不是
# 4
# 次，则需要在最终答案中包含该字符
# 3
# 次。
#
# 你可以按任意顺序返回答案。
#
#
#
# 示例
# 1：
#
# 输入：["bella", "label", "roller"]
# 输出：["e", "l", "l"]
#
# 示例
# 2：
#
# 输入：["cool", "lock", "cook"]
# 输出：["c", "o"]
class Solution:
    def commonChars(self, A):
        ans = {}
        for j in A[0]:
            ans[j] = ans.get(j, 0) + 1

        for i in range(1,len(A)):
            a = {}
            for j in A[i]:
                a[j] = a.get(j,0)+1
            for key in a:
                if key in ans:
                    ans[key] = min(ans[key],a[key])
            for key in ans:
                if key not in a:
                    ans[key]  =0
        res = ""
        ress = []
        for i in ans:
            res = res+i*ans[i]
        for i in res:
            ress.append(i)
        return ress


s=Solution()
print(s.commonChars(["bella", "label", "roller"]))

