class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2 != 0:
            return 'a'*n
        return 'a'*(n-1) + 'b'
print(Solution().generateTheString(4))
print(Solution().generateTheString(2))
print(Solution().generateTheString(7))
print(Solution().generateTheString(1))
print(Solution().generateTheString(6))
