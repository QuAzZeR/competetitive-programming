class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        l = len(ring)

        def dfs(ring, i):
            if i == len(key):
                return 0
            answer = 1000**3
            for j in range(l):
                w = ring[j]
                if w == key[i]:
                    m = min(j, l - j)
                    r = dfs(ring[j:] + ring[:j], i + 1)
                    answer = min(answer, m + r)
            return answer

        return dfs(ring, 0) + len(key)


print(Solution().findRotateSteps("godding", "gd"))
print(Solution().findRotateSteps("godding", "godding"))
