from typing import List
import unittest


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        self.answer = 0
        m = 0
        def bit_op(idx, v):
            print(">>>", idx, v,m)
            if v == m :
                self.answer += 1

            for i in range(idx, n):
                bit_op(i+1, v | nums[i])
            return

        if len(set(nums)) == 1:
            return 2 ** n -1

        for i in nums:
            m |=  i
        bit_op(0, 0)
        return self.answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.countMaxOrSubsets([3,1]), 2)
        self.assertEqual(s.countMaxOrSubsets([2,2,2]), 7)
        self.assertEqual(s.countMaxOrSubsets([3,2,1,5]), 6)


if __name__ == "__main__":
    unittest.main()
