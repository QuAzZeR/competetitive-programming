from typing import List
import unittest


class Solution:
    def kthCharacter(self, k: int) -> str:
        answer = "a"

        while len(answer) < k:
            n = ""
            for i in range(len(answer)):
                if answer[i] == 'z':
                    n += 'a'
                else:
                    n += chr(ord(answer[i])+1)
            answer += n
        return answer[k-1]


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.kthCharacter(5), "b")
        self.assertEqual(s.kthCharacter(10), "c")


if __name__ == "__main__":
    unittest.main()
