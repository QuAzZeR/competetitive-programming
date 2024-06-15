class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ls = sorted(list(s))
        lt = sorted(list(t))
        n = min(len(ls), len(lt))
        for i in range(n):
            if ls[i] != lt[i]:
                if n == len(ls):
                    return lt[i]
                else:
                    return ls[i]
        if n == len(ls):
            return lt[-1]
        return ls[-1]


print(Solution().findTheDifference("abcd", "abcde"))
print(Solution().findTheDifference("", "y"))
