class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        answer = 0
        while num1 != 0 and num2 != 0:
            if num1 <= num2:
                num2 -= num1
            else:
                num1 -= num2
            answer += 1
        return answer

print(Solution().countOperations(2,3))
print(Solution().countOperations(10,10))
