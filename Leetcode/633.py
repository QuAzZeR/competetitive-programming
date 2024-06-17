from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(sqrt(c)) + 1):
            b = sqrt(c - i * i)
            if b == int(b):
                return True
        return False


print(Solution().judgeSquareSum(5))
print(Solution().judgeSquareSum(3))
print(Solution().judgeSquareSum(1))
print(Solution().judgeSquareSum(999999999))
