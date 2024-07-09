from typing import List
import unittest


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = customers[0][0] + customers[0][1]
        sum_waiting_time = customers[0][1]
        n = len(customers)
        for i in range(1, n):
            arrival, time = customers[i]
            if arrival < current_time:
                sum_waiting_time += (current_time + time) - arrival
                current_time += time
            else:
                sum_waiting_time += time
                current_time = arrival + time

        return sum_waiting_time / n


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.averageWaitingTime([[1, 2], [2, 5], [4, 3]]), 5.0)
        self.assertEqual(s.averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]), 3.25)


if __name__ == "__main__":
    unittest.main()
