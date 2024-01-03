class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        answer = 0
        for i in range(2, n*2+1):
            if i%2 == 0 and i%n == 0:
                answer = i
                break
        return answer
print(Solution().smallestEvenMultiple(5))
print(Solution().smallestEvenMultiple(6))
