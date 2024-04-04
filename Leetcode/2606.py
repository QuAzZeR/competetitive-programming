from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        cost = {chr(i): i - 96 for i in range(97, 123)}
        n = len(s)
        for i in range(len(chars)):
            cost[chars[i]] = vals[i]
        d = [0] * (n)
        for i in range(n):
            if i >= 1:
                d[i] = max([0, cost[s[i]], d[i - 1] + cost[s[i]]])
            else:
                d[i] = max([0, cost[s[i]]])
        return max(d)


print(Solution().maximumCostSubstring("adaa", "d", [-1000]))
print(Solution().maximumCostSubstring("abc", "abc", [-1, -1, -1]))
print(Solution().maximumCostSubstring("kqqqqqkkkq", "kq", [-6, 6]))
