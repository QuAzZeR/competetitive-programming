from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        answer = [""]*n
        d = {score[i]: i for i in range(n)}
        m = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal"
        }
        score.sort(reverse=True)
        for i in range(n):
            s = score[i]
            if i <= 2:
                answer[d[s]] = m[i]
            else:
                answer[d[s]] = str(i+1)
        return answer

print(Solution().findRelativeRanks([5,4,3,2,1]))
print(Solution().findRelativeRanks([10,3,8,9,4]))