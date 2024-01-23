from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        x = [i for i in nums if i != 0]
        lx = len(x)
        for i in range(lx):
            nums[i] = x[i]
        for i in range(l - lx):
            nums[lx+i] =0


