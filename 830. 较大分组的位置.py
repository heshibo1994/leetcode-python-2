# 在一个由小写字母构成的字符串 S 中，包含由一些连续的相同字符所构成的分组。
#
# 例如，在字符串 S = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
#
# 我们称所有包含大于或等于三个连续字符的分组为较大分组。找到每一个较大分组的起始和终止位置。
#
# 最终结果按照字典顺序输出。
# 示例 3:
#
# 输入: "abcdddeeeeaabbbcd"
# 输出: [[3,5],[6,9],[12,14]]
class Solution:
    def largeGroupPositions(self, S):
        left = 0
        right =1
        ans = []
        while right<len(S):
            if S[left] == S[right]:
                right += 1
            else:
                if right - left>2:
                    ans.append([left,right-1])
                left = right
                right = left+1
        if right - left > 2:
            ans.append([left, right - 1])
        return ans
s=Solution()
print(s.largeGroupPositions("aaa"))
print(s.largeGroupPositions("abcdddeeeeaabbbcd"))