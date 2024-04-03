from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)
        self.answer = None

        def travel(i, j, iw):
            if iw == w:
                return True
            if i < 0:
                return False
            if i >= m:
                return False
            if j < 0:
                return False
            if j >= n:
                return False
            if board[i][j] != word[iw]:
                return False
            temp = board[i][j]
            board[i][j] = ""
            if (
                travel(i, j + 1, iw + 1)
                or travel(i, j - 1, iw + 1)
                or travel(i + 1, j, iw + 1)
                or travel(i - 1, j, iw + 1)
            ):
                return True
            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if travel(i, j, 0):
                    return True

        return False


print(
    Solution().exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
    )
)

print(
    Solution().exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
    )
)
print(
    Solution().exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
    )
)
