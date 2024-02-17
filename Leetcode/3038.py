from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        previous = nums[0] + nums[1]
        count = 0
        l = len(nums)
        while l > 1:
            current = nums[0] + nums[1]
            if current == previous:
                nums = nums[2:]
            else:
                break
            l = len(nums)
            count += 1
        return count


print(Solution().maxOperations([3, 2, 1, 4, 5]))
print(Solution().maxOperations([3, 2, 6, 1, 4]))
