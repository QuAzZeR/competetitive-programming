from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.answer = []
        n = len(s)

        def is_palindrome(s):
            return s == s[::-1]

        def partitioning(start, path):
            if start == n:
                self.answer.append(path)
                return
            for end in range(start + 1, n + 1):
                if is_palindrome(s[start:end]):
                    partitioning(end, path + [s[start:end]])

        partitioning(0, [])
        return self.answer


print(Solution().partition("aab"))
print(Solution().partition("a"))
