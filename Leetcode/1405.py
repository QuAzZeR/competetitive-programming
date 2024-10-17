from typing import List
import unittest
from heapq import heappush, heappop


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        answer = []
        h  = []
        if a > 0:
            heappush(h, (-a, 'a'))
        if b > 0:
            heappush(h, (-b, 'b'))
        if c > 0:
            heappush(h, (-c, 'c'))

        while h:
            cnt_1, c_1 = heappop(h)
            if len(answer) >= 2 and answer[-1] == answer[-2] == c_1:
                if not h:
                    break
                cnt_2, c_2 = heappop(h)
                answer.append(c_2)
                if cnt_2 +1 < 0:
                    heappush(h, (cnt_2 + 1, c_2))
                heappush(h, (cnt_1, c_1))
            else:
                answer.append(c_1)
                if cnt_1 + 1 < 0:
                    heappush(h, (cnt_1 + 1, c_1))

        return ''.join(answer)


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.longestDiverseString(1,1,7), "ccaccbcc")
        self.assertEqual(s.longestDiverseString(7,1,0), "aabaa")


if __name__ == "__main__":
    unittest.main()
