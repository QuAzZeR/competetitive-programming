from typing import List
import unittest


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_and_score(text, first, second, points):
            stack = []
            score = 0
            for c in text:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(c)
            remaining = "".join(stack)
            return remaining, score

        answer = 0
        if x >= y:
            remain, score = remove_and_score(s, "a", "b", x)
            answer += score
            _, score = remove_and_score(remain, "b", "a", y)
            answer += score
        else:
            remain, score = remove_and_score(s, "b", "a", y)
            answer += score
            _, score = remove_and_score(remain, "a", "b", x)
            answer += score
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.maximumGain("cdbcbbaaabab", 4, 5), 19)
        self.assertEqual(s.maximumGain("aabbaaxybbaabb", 5, 4), 20)


if __name__ == "__main__":
    unittest.main()
