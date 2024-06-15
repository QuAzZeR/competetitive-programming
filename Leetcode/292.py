class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


print(Solution().canWinNim(4))
print(Solution().canWinNim(1))
print(Solution().canWinNim(2))
