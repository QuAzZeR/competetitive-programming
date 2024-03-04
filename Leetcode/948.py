from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        score = 0
        max_score = 0
        l = 0
        r = n - 1

        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break

        return max_score


print(Solution().bagOfTokensScore([100], 50))
print(Solution().bagOfTokensScore([200, 100], 150))
print(Solution().bagOfTokensScore([100, 200, 300, 400], 200))
