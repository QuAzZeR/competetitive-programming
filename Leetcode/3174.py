class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)
        answer = ""
        for i in range(n):
            if s[i] in "0123456789":
                if i != 0:
                    answer = answer[:-1]

            else:
                answer += s[i]
        return answer


print(Solution().clearDigits("abc"))
print(Solution().clearDigits("34"))
print(Solution().clearDigits("abc12"))
