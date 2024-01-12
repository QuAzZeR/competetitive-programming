class Solution:
    def totalMoney(self, n: int) -> int:
        answer = 0
        current = 0
        while n > 0:
            if n >= 7:
                answer += 7*((7+current) + (1+current))//2
                current += 1
            else:
                answer +=  n*((n+current) + (1+current))//2
            n-= 7
        return answer

print(Solution().totalMoney(4))
print(Solution().totalMoney(10))
print(Solution().totalMoney(20))
