# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#
#     数字 1-9 在每一行只能出现一次。
#     数字 1-9 在每一列只能出现一次。
#     数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-sudoku
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 每行
        for i in range(len(board)):
            if not self.isValid(board[i]):
                return False
        # 每列
        for i in range(9):
            l = [board[j][i] for j in range(9)]

            if not self.isValid(l):
                return False
        # 3*3
        for i in range(3):
            for j in range(3):
                grid_3 = board[i*3:(i+1)*3]
                l = []
                for g in grid_3:
                    l.extend(g[j * 3:(j + 1) * 3])
                if not self.isValid(l):
                    return False
        return True

    def isValid(self,l):
        a = []
        for i in l:
            if i != ".":
                if i not in a:
                    a.append(i)
                else:
                    return False
        return True
s=Solution()
print(s.isValidSudoku([ ["5","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."], ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"], [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"] ]))

print(s.isValidSudoku([   ["8","3",".",".","7",".",".",".","."],   ["6",".",".","1","9","5",".",".","."],   [".","9","8",".",".",".",".","6","."],   ["8",".",".",".","6",".",".",".","3"],   ["4",".",".","8",".","3",".",".","1"],   ["7",".",".",".","2",".",".",".","6"],   [".","6",".",".",".",".","2","8","."],   [".",".",".","4","1","9",".",".","5"],   [".",".",".",".","8",".",".","7","9"] ]))

