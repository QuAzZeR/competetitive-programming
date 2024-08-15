from typing import List
import unittest


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five += 1
            if i == 10:
                ten += 1
                five -= 1
            if i == 20:
                if ten > 0:
                    five -= 1
                    ten -=1
                else:
                    five -= 3
            if five < 0 or ten < 0:
                return False

        return True


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.lemonadeChange([5,5,5,10,20]), True)
        self.assertEqual(s.lemonadeChange([5,5,10,10,20]), False)
        self.assertEqual(s.lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]), True)


if __name__ == "__main__":
    unittest.main()
