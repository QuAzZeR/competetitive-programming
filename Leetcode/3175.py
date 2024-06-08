from typing import List


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if k >= n:
            players = [(i, skills[i]) for i in range(n)]
            return max(players, key=lambda x: x[1])[0]
        win_count = 0
        current_winner = -1
        for i in range(1, n * 2):
            c = i % n
            # print(i, current_winner, c, skills[current_winner], skills[c], win_count)
            if i == 1:
                current_winner = 0 if skills[0] > skills[1] else 1
                win_count = 1

                if win_count == k:
                    break
                continue
            if skills[current_winner] > skills[c]:
                win_count += 1
            else:
                current_winner = c
                win_count = 1
            if win_count == k:
                break
        return current_winner


print(Solution().findWinningPlayer([4, 2, 6, 3, 9], 2))
print(Solution().findWinningPlayer([2, 5, 4], 3))
print(Solution().findWinningPlayer([1, 2, 4], 2))
print(Solution().findWinningPlayer([4, 18, 17, 20, 15, 12, 8, 5], 1))
