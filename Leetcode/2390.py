class Solution:
    def removeStars(self, s: str) -> str:
        answer = []
        for i in s:
            if i == "*":
                if len(answer) > 0:
                    answer.pop()
            else:
                answer.append(i)
        return "".join(answer)


print(Solution().removeStars("leet**cod*e"))
print(Solution().removeStars("erase*****"))
print(Solution().removeStars("*****erase"))
