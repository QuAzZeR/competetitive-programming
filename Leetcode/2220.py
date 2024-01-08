class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        answer = 1
        return bin(start^goal).count('1')
print(Solution().minBitFlips(10, 7))
print(Solution().minBitFlips(3, 4))
