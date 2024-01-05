class Solution:
    def countDigits(self, num: int) -> int:
        return len([i for i in str(num) if num%int(i) == 0])
print(Solution().countDigits(2))
print(Solution().countDigits(121))
print(Solution().countDigits(1248))

