from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = []
        self.dfs(n, "", 0, 0)
        return self.answer

    def dfs(self, n, p, o, c):
        if len(p) == n * 2:
            if p.count("(") != p.count(")"):
                return
            self.answer.append(p)
            return
        if o < n:
            self.dfs(n, p + "(", o + 1, c)
        if c < o:
            self.dfs(n, p + ")", o, c + 1)


print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(1))
