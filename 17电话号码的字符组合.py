# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dit = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'],
               "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}
        ans = []
        def dfs(i, word):
            if i == len(digits):
                ans.append(word)
                return
            for w in dit[digits[i]]:
                word = word + w
                dfs(i+1, word)
                word = word[:-1]
        dfs(0, "")
        return ans
s =Solution()
print(s.letterCombinations("234"))