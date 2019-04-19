# 我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。
#
# 如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。
#
# 现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？

class Solution:
    def rotatedDigits(self, N):
        ans = 0
        for i in range(1,N+1):
            if self.good(i):
                ans =ans+1
        return ans
    def good(self,n):
        temp = ""
        for i in str(n):
            if i in  ["0","1","8"]:
                temp = temp+i
            elif i in ["6","9"]:
                temp = temp+ str(15-int(i))
            elif i in ["2","5"]:
                temp = temp+  str(7-int(i))
            else:
                return False
        if temp!=str(n):
            print(n, "是")
            return True
s =Solution()
print(s.rotatedDigits(10))