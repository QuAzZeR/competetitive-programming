from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        new_nums = sorted([i for i in nums if i != 0], reverse=True)
        n = len(nums)
        nn = len(new_nums)
        if nn < 3:
            return 0
        first = new_nums[0] * new_nums[1] * new_nums[2]
        if n != nn and new_nums[0] < 0:
            return 0

        last = new_nums[-2] * new_nums[-1] * new_nums[0]
        if first > last:
            return first
        elif n > nn and first < 0 and last < 0:
            return 0
        else:
            return last


print(Solution().maximumProduct([1, 2, 3]))
print(Solution().maximumProduct([1, 2, 3, 4]))
print(Solution().maximumProduct([-1, -2, -3]))
print(Solution().maximumProduct([4, -1, -2, -3]))
print(Solution().maximumProduct([-3, -2, -1, 0, 0, 0, 0]))
print(Solution().maximumProduct([1, 0, 100]))
print(Solution().maximumProduct([3, 4, 0, 0, -1, -5]))
print(Solution().maximumProduct([0, -1, 2, 3]))
