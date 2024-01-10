class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = ''
        c = 0
        for i in s:
            if i == '(':
                if c != 0:
                    answer += i
                c += 1
            else:
                c -= 1
                if c != 0:
                    answer += i
        return answer

print(Solution().removeOuterParentheses("(()())(())"))
print(Solution().removeOuterParentheses("(()())(())(()(()))"))
print(Solution().removeOuterParentheses("()()"))
