from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        winner = "Pending"

        table = [[""] * 3 for i in range(3)]
        players = ["A", "B"]
        for i in range(len(moves)):
            x, y = moves[i]
            if i % 2 == 0:
                table[x][y] = "A"
            else:
                table[x][y] = "B"
        for i in range(3):
            if (
                table[i][0] in players
                and table[i][0] == table[i][1]
                and table[i][1] == table[i][2]
            ):
                winner = table[i][0]
                break
            if (
                table[0][i] in players
                and table[0][i] == table[1][i]
                and table[1][i] == table[2][i]
            ):
                winner = table[0][i]
                break
        if (
            table[1][1] in players
            and table[0][0] == table[1][1]
            and table[1][1] == table[2][2]
        ):
            winner = table[1][1]
        if (
            table[1][1] in players
            and table[0][2] == table[1][1]
            and table[1][1] == table[2][0]
        ):
            winner = table[1][1]
        if winner not in players and len(moves) == 9:
            return "Draw"
        return winner


print(Solution().tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))
print(Solution().tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))
print(
    Solution().tictactoe(
        [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
    )
)
print(Solution().tictactoe([[0, 0], [0, 1], [2, 1]]))
