from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        target = 0

        nums = sorted(nums)
        n = len(nums)
        for first in range(n):
            middle = first + 1
            last = n - 1
            while middle < last:
                s = nums[first] + nums[middle] + nums[last]
                if s == target:
                    answer.add((nums[first], nums[middle], nums[last]))
                    middle += 1
                    last -= 1
                elif s < target:
                    middle += 1
                else:
                    last -= 1
        return list(answer)


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([0, 1, 1]))
print(Solution().threeSum([0, 0, 0]))
