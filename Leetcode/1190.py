from typing import List
import unittest


class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = [""]
        index = 0
        for i in range(n):
            if s[i] == "(":
                stack.append("")
                index += 1
                continue
            elif s[i] == ")":
                temp = stack.pop()[::-1]
                stack[index - 1] += temp
                index -= 1
            else:
                stack[index] += s[i]
        return stack[0]


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.reverseParentheses("(abcd)"), "dcba")
        self.assertEqual(s.reverseParentheses("(u(love)i)"), "iloveu")
        self.assertEqual(s.reverseParentheses("(ed(et(oc))el)"), "leetcode")
        self.assertEqual(s.reverseParentheses("sxmdll(q)eki(x)"), "sxmdllqekix")


if __name__ == "__main__":
    unittest.main()
