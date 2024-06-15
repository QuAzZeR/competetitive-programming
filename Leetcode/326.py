class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        for i in range(n):
            x = 3**i
            if x == n:
                return True
            if x > n:
                return False
        return False


print(Solution().isPowerOfThree(27))
print(Solution().isPowerOfThree(0))
print(Solution().isPowerOfThree(-1))
print(Solution().isPowerOfThree(1))
print(Solution().isPowerOfThree(59048))
