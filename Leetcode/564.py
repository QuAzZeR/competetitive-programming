from typing import List
import unittest


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        if n == "1":
            return "0"
        prefix = n[:(l+1)//2]
        prefix_number = int(prefix)
        possible_answer = set()
        for i in [-1, 0, 1]:
            new_prefix = str(prefix_number + i)
            if l %2 == 0:
                possible_answer.add(new_prefix +new_prefix[::-1])
            else:
                possible_answer.add( new_prefix +new_prefix[:-1][::-1])
        possible_answer.add(str(10**(l-1)-1))
        possible_answer.add(str(10**(l)+1))
        possible_answer.discard(n)
        answer = min(possible_answer, key = lambda x: (abs(int(x) - int(n)), int(x)))
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.nearestPalindromic("123"), "121")
        self.assertEqual(s.nearestPalindromic("1"), "0")
        self.assertEqual(s.nearestPalindromic("4"), "3")


if __name__ == "__main__":
    unittest.main()
