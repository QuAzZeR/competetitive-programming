from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = None
        df = 0

        nums = sorted(nums)
        n = len(nums)
        for first in range(n):
            middle = first + 1
            last = n - 1
            while middle < last:
                s = nums[first] + nums[middle] + nums[last]
                if s == target:
                    answer = s
                    return s
                elif s < target:
                    if answer is None:
                        answer = s
                        df = abs(target - s)
                    if abs(target - s) < df:
                        answer = s
                        df = abs(target - s)
                    middle += 1
                else:
                    if answer is None:
                        answer = s
                        df = abs(target - s)
                    if abs(target - s) < df:
                        answer = s
                        df = abs(target - s)
                    last -= 1
        return answer


print(Solution().threeSumClosest([-1, 1, 2, -4], 1))
print(Solution().threeSumClosest([0, 0, 0], 1))
