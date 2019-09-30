# 给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
#
# 假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
#
# 注意：每次拼写时，chars 中的每个字母都只能用一次。
#
# 返回词汇表 words 中你掌握的所有单词的 长度之和。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def countCharacters(self, words, str):
        words_map = []
        a = {}
        ans =[]
        for i in str:
            a[i] = a.get(i,0)+1
        for j in words:
            temp = {}
            for w in j:
                temp[w] = temp.get(w,0)+1
            words_map.append(temp)
        for wm in words_map:
            flag = True
            for w in wm.keys():
                if wm[w]>=a.get(w,0):
                    flag = False
                    break
            if flag:
                ans.append(wm)



        print(a)
        print(ans)
s = Solution()
print(s.countCharacters(["cat","bt","hat","tree"],  "atach"))