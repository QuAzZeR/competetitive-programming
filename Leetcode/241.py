from typing import List
import unittest


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        answer = []
        n = len(expression)
        for i in range(n):
            op = expression[i]
            if op in '+-*':
                s1 = expression[0:i]
                s2 = expression[i+1:]
                s1 = self.diffWaysToCompute(s1)
                s2 = self.diffWaysToCompute(s2)
                for i in s1:
                    for j in s2:
                        if op == "*":
                            answer.append(int(i) * int(j))
                        if op == "+":
                            answer.append(int(i) + int(j))
                        if op == "-":
                            answer.append(int(i) - int(j))
        if len(answer) == 0:
            answer.append(int(expression))
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.diffWaysToCompute("2-1-1"), [0,2])
        self.assertEqual(s.diffWaysToCompute("2*3-4*5"), [-34,-14,-10,-10,10])


if __name__ == "__main__":
    unittest.main()
