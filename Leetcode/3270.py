from typing import List
import unittest


class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        n = [f'{num1:04}', f'{num2:04}', f'{num3:04}']
        answer = ""
        for i in range(4):
            answer += min([n[j][i] for j in range(3)])
        return int(answer)


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.generateKey(1, 10, 1000), 0)
        self.assertEqual(s.generateKey(987, 879, 798), 777)
        self.assertEqual(s.generateKey(1, 2 , 3), 1)


if __name__ == "__main__":
    unittest.main()
