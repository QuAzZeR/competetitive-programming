from typing import List
import unittest


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        self.mergeSort(nums, 0, len(nums) -1)
        return nums

    def mergeSort(self, nums, left, right):
        if left >= right:
            return
        mid = left + (right - left)//2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid+1, right)
        self.merge(nums, left, mid, right)
    def merge(self, nums, left, mid, right):
        left_array = nums[left:mid+1]
        right_array = nums[mid+1: right+1]
        l = 0
        r = 0
        k = left
        while l < len(left_array) and r < len(right_array):
            if left_array[l] <= right_array[r]:
                nums[k] = left_array[l]
                l += 1
            else:
                nums[k] = right_array[r]
                r += 1
            k += 1

        while  l < len(left_array):
            nums[k] = left_array[l]
            l += 1
            k += 1

        while  r < len(right_array):
            nums[k] = right_array[r]
            r += 1
            k += 1


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.sortArray([5,2,3,1]), [1,2,3,5])
        self.assertEqual(s.sortArray([5,1,1,2,0,0]), [0,0,1,1,2,5])
        self.assertEqual(s.sortArray([-2,3,-5]), [-5,-2,3])


if __name__ == "__main__":
    unittest.main()
