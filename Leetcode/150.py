from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token in "+-*/":
                b = s.pop()
                answer = s.pop()
                if token == "+":
                    answer += b
                elif token == "-":
                    answer -= b
                elif token == "*":
                    answer *= b
                elif token == "/":
                    answer = int(answer / b)
                s.append(answer)
            else:
                s.append(int(token))
        return s[-1]


print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
print(
    Solution().evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
print(Solution().evalRPN(["18"]))
