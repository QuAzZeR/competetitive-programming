class Solution:
    def sumBase(self, n: int, k: int) -> int:
        answer = 0
        while n != 0:
            answer += n%k
            n //= k
        return answer

print(Solution().sumBase(34,6))
print(Solution().sumBase(10,10))
print(Solution().sumBase(72,3))

