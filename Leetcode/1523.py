class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        return (high - low) // 2 + 1


print(Solution().countOdds(3, 7))
print(Solution().countOdds(8, 10))
print(Solution().countOdds(1, 10))
print(Solution().countOdds(2, 10))
