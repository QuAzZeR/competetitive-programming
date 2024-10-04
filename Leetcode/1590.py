from typing import List
import unittest


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        r = s %p
        if r == 0:
            return 0
        prefix_mod = {0: -1}
        prefix_sum = 0
        m = len(nums)
        for i in range(len(nums)):
            prefix_sum += nums[i]
            current_mod = prefix_sum % p
            target_mod = (current_mod - r + p) % p
            if target_mod in prefix_mod:
                m = min(m, i - prefix_mod[target_mod])
            prefix_mod[current_mod] = i

        return m if m < len(nums) else -1


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minSubarray([3,1,4,2], 6), 1)
        self.assertEqual(s.minSubarray([6,3,5,2], 9), 2)
        self.assertEqual(s.minSubarray([1,2,3], 3), 0)


if __name__ == "__main__":
    unittest.main()
