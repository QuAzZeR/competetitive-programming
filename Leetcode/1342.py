class Solution:
    def numberOfSteps(self, num: int) -> int:
        answer = 0
        while num !=0:
            if num%2 == 0:
                num = int(num/2)
            else:
                num -= 1
            answer += 1
        return answer

print(Solution().numberOfSteps(14))
print(Solution().numberOfSteps(8))
print(Solution().numberOfSteps(123))
