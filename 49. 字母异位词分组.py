# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
class Solution:
    def groupAnagrams(self, strs):
        ans = []
        res = []
        for i in range(len(strs)):
            temp ={}
            for j in strs[i]:
                temp[j] = temp.get(j,0)+1
            if temp not in ans:
                ans.append(temp)
            else:

