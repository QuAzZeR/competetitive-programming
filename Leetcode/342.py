class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        for i in range(n):
            x = 4**i
            if x == n:
                return True
            if x > n:
                return False
        return False


print(Solution().isPowerOfFour(16))
print(Solution().isPowerOfFour(5))
print(Solution().isPowerOfFour(1))
