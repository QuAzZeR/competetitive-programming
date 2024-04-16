class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        answer = 0
        for i in range(len(number)):
            if number[i] == digit:
                answer = max(answer, int("".join(number[0:i] + number[i + 1 :])))

        return str(answer)


print(Solution().removeDigit("123", "3"))
print(Solution().removeDigit("1231", "1"))
print(Solution().removeDigit("551", "5"))
