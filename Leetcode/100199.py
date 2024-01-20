from typing import List
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if nums[j+1] < nums[j] and bin(nums[j+1]).count('1') == bin(nums[j]).count('1'):
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
        return sorted(nums) == nums

print(Solution().canSortArray([8,4,2,30,15]))
print(Solution().canSortArray([1,2,3,4,5]))
print(Solution().canSortArray([3,16,8,4,2]))
print(Solution().canSortArray([75,34,30]))
