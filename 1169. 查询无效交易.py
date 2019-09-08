# 如果出现下述两种情况，交易
# 可能无效：
#
# 交易金额超过 ¥1000
# 或者，它和另一个城市中同名的另一笔交易相隔不超过
# 60
# 分钟（包含
# 60
# 分钟整）
#
# 每个交易字符串
# transactions[i]
# 由一些用逗号分隔的值组成，这些值分别表示交易的名称，时间（以分钟计），金额以及城市。
#
# 给你一份交易清单
# transactions，返回可能无效的交易列表。你可以按任何顺序返回答案。
#
#
#
# 示例
# 1：
#
# 输入：transactions = ["alice,20,800,mtv", "alice,50,100,beijing"]
# 输出：["alice,20,800,mtv", "alice,50,100,beijing"]
# 解释：第一笔交易是无效的，因为第二笔交易和它间隔不超过
# 60
# 分钟、名称相同且发生在不同的城市。同样，第二笔交易也是无效的。
#
# 示例
# 2：
#
# 输入：transactions = ["alice,20,800,mtv", "alice,50,1200,mtv"]
# 输出：["alice,50,1200,mtv"]
#
# 来源：力扣（LeetCode）
# 链接：https: // leetcode - cn.com / problems / invalid - transactions
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def invalidTransactions(self, transactions):
        ans = [0] *len(transactions)
        for i in range(len(transactions)):
            name_i,time_i,money_i,city_i = transactions[i].split(",")
            if int(money_i) >1000:
                ans[i] = 1
            for j in range(len(transactions)):
                name_j, time_j, money_j, city_j = transactions[j].split(",")
                if name_i == name_j and city_i!=city_j and abs(int(time_i)-int(time_j))<=60:
                    ans[i],ans[j] =1,1
        return [transactions[i] for i in range(len(ans)) if ans[i]==1]
s = Solution()
print(s.invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))







