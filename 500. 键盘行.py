# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
#
#
#
# American
# keyboard
#
# 示例：
#
# 输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]
class Solution:
    def findWords(self, words):
        key = 'abcdefghijklmnopqrstuvwxyz'
        value = [2,3,3,2,1,2,2,2,1,2,2,2,3,3,1,1,1,1,2,1,1,3,1,3,1,3]
        a = dict(zip(key,value))
        print(a)
        ans = []
        for i in words:
            temp = a[i[0].lower()]
            flag = True
            for w in range(1,len(i)):
                if a[i[w].lower()]!=temp:
                    flag = False
                    break
            if flag:
                ans.append(i)
        print(ans)
s=Solution()
s.findWords(["Hello", "Alaska", "Dad", "Peace"])
