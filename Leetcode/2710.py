class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return str(int(num[::-1]))[::-1]


print(Solution().removeTrailingZeros("51230100"))
print(Solution().removeTrailingZeros("123"))
