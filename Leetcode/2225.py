from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = {}
        loser = {}
        for i in range(len(matches)):
            w, l = matches[i]
            if w not in winner:
                winner[w] = []
            winner[w].append(l)
            if l not in loser:
                loser[l] = []
            loser[l].append(w)
        player = sorted(list(set(list(winner.keys()) + list(loser.keys()))))
        no_lose = [i for i in player if i not in loser]
        lose_1 = [i for i in loser if i in loser and len(loser[i]) == 1]
        return [no_lose, lose_1]

print(Solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(Solution().findWinners([[2,3],[1,3],[5,4],[6,4]]))
