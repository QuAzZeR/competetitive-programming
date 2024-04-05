class Solution:
    def makeGood(self, s: str) -> str:
        answer = []
        i = 0
        for i in s:
            if answer and abs(ord(i) - ord(answer[-1])) == 32:
                answer.pop()
            else:
                answer.append(i)
        return "".join(answer)


print(Solution().makeGood("leEeetcode"))
print(Solution().makeGood("abBAcC"))
print(Solution().makeGood("s"))
