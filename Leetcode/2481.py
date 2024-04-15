class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 != 0:
            return n
        else:
            return n // 2


print(Solution().numberOfCuts(4))
print(Solution().numberOfCuts(3))
print(Solution().numberOfCuts(1))
