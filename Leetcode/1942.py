from typing import List
from heapq import heappush, heappop
import unittest


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        orders = sorted(range(n), key=lambda x: times[x][0])
        empty_seats = list(range(n))
        taken_seats = []
        for i in orders:
            arrival, leave = times[i]
            while taken_seats and taken_seats[0][0] <= arrival:
                heappush(empty_seats, heappop(taken_seats)[1])
            seat = heappop(empty_seats)
            if i == targetFriend:
                return seat
            heappush(taken_seats, (leave, seat))
        return 0


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.smallestChair([[1,4],[2,3],[4,6]], 1), 1)
        self.assertEqual(s.smallestChair([[3,10],[1,5],[2,6]], 0), 2)


if __name__ == "__main__":
    unittest.main()
