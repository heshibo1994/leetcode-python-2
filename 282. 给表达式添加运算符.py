# 给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加二元运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。
#
# 示例 1:
#
# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"]
#
# 示例 2:
#
# 输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"]
#
# 示例 3:
#
# 输入: num = "105", target = 5
# # 输出: ["1*0+5","10-5"]
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans =[]
        if len(num)==0:
            return ans
        for i in range(1,len(num)):
            fos = num[0:i]
            fol = int(fos)
            if ()
