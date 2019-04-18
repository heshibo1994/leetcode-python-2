# 所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
#
# 编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。
#
# 示例:
#
# 输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#
# 输出: ["AAAAACCCCC", "CCCCCAAAAA"]
#
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        st = set()
        ret = set()
        for i in range(n-9):
            cur = s[i:i+10]
            if cur in st:
                ret.add(cur)
            else:
                st.add(cur)
        return list(ret)

s =Solution()
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))

print(s.findRepeatedDnaSequences("AAAAAAAAAAAA"))