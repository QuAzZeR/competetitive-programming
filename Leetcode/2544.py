class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        answer = 0
        for i in range(len(s)):
            if i % 2 != 0:
                answer += -int(s[i])
            else:
                answer += int(s[i])
        return answer


print(Solution().alternateDigitSum(521))
print(Solution().alternateDigitSum(111))
print(Solution().alternateDigitSum(886996))
