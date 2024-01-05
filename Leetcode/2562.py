class Solution:
    def sumOfMultiples(self, n: int) -> int:
        answer = 0
        for i in range(1,n+1):
            if i%3 == 0 or i%5 == 0 or i%7 == 0:
                answer += i
        return answer

print(Solution().sumOfMultiples(7))
print(Solution().sumOfMultiples(10))
print(Solution().sumOfMultiples(9))
