class Solution:
    def numSteps(self, s: str) -> int:
        c = 0
        answer = 0
        l = len(s) - 1
        while l > 0:
            if int(s[l]) + c == 0:
                c = 0
                answer += 1

            elif int(s[l]) + c == 2:
                c = 1
                answer += 1
            else:
                c = 1
                answer += 2
            l -= 1
        if c == 1:
            answer += 1
        return answer


print(Solution().numSteps("1101"))
print(Solution().numSteps("10"))
