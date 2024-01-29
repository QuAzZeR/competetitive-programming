from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = Counter(text)
        for i in d:
            if 'o' == i:
                d[i] //= 2
            if 'l' == i:
                d[i] //= 2
        m = [d[i] for i in d if i in 'balon']

        if len(m) < 5:
            return 0
        return min(m)

print(Solution().maxNumberOfBalloons("nlaebolko"))
print(Solution().maxNumberOfBalloons("loonbalxballpoon"))
print(Solution().maxNumberOfBalloons("leetcode"))
print(Solution().maxNumberOfBalloons("lloo"))
