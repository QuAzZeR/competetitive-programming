class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d = {}
        for i in range(len(s)):
            d[s[i]] = [i]
        for i in range(len(s)):
            d[t[i]].append(i)
        return sum([abs(d[i][0] - d[i][1]) for i in d])


print(Solution().findPermutationDifference("abc", "bac"))
print(Solution().findPermutationDifference("abcde", "edbac"))
