class Solution:
    def countAsterisks(self, s: str) -> int:
        check = False
        answer = 0
        for i in s:
            if not check:
                if i == '*' :
                    answer += 1
            if i == '|':
                check = not check

        return answer

print(Solution().countAsterisks("l|*e*et|c**o|*de|"))
print(Solution().countAsterisks("iamprogrammer"))
print(Solution().countAsterisks("yo|uar|e**|b|e***au|tifu|l"))
