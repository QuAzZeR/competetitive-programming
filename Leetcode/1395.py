from typing import List
import unittest


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        answer = 0
        n = len(rating)
        for i in range(n):
            r_min = 0
            r_max = 0
            l_min = 0
            l_max = 0
            for j in range(i+1, n):
                if rating[j] < rating[i]:
                    r_min += 1
                elif rating[j] > rating[i]:
                    r_max += 1
            for j in range(i):
                if rating[j] < rating[i]:
                    l_min += 1
                if rating[j] > rating[i]:
                    l_max += 1
            answer += r_min * l_max + r_max * l_min

        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.numTeams([2,5,3,4,1]), 3)
        self.assertEqual(s.numTeams([2,1,3]), 0)
        self.assertEqual(s.numTeams([1,2,3,4]), 4)


if __name__ == "__main__":
    unittest.main()
