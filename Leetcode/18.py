from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = set()

        nums = sorted(nums)
        n = len(nums)
        for first in range(n):
            for second in range(first + 1, n):
                third = second + 1
                fourth = n - 1
                while third < fourth:
                    s = nums[first] + nums[second] + nums[third] + nums[fourth]
                    if s == target:
                        answer.add(
                            (nums[first], nums[second], nums[third], nums[fourth])
                        )
                        third += 1
                        fourth -= 1
                    elif s < target:
                        third += 1
                    else:
                        fourth -= 1
        return list(answer)


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
print(Solution().fourSum([2, 2, 2, 2, 2], 8))
