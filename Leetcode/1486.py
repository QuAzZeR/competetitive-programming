class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        answer = start
        current = start
        for i in range(n-1):
            current = current + 2
            answer ^= current
        return answer

print(Solution().xorOperation(5,0))
print(Solution().xorOperation(4,3))
