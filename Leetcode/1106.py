from typing import List
import unittest


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        m = {
            "f": False,
            "t": True
        }
        s = []

        for e in expression:
            if e != ')' and e != ',':
                s.append(e)
            elif e == ')':
                exp = []
                while s and s[-1] != '(':
                    exp.append(m[s.pop()])
                s.pop()
                if s:
                    op = s.pop()
                    r = exp[0]
                    if op == '&':
                        for ex in exp:
                            r &= ex
                    elif op == '|':
                        for ex in exp:
                            r |= ex
                    else:
                        r = not r
                    s.append('t' if r else 'f')



        return s[-1] == 't'


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.parseBoolExpr("&(|(f))"), False)
        self.assertEqual(s.parseBoolExpr("|(f,f,f,t)"), True)
        self.assertEqual(s.parseBoolExpr("!(&(f,t))"), True)


if __name__ == "__main__":
    unittest.main()
