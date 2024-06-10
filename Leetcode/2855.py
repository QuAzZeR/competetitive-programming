from typing import List
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        if nums == sorted(nums):
            return 0
            a = nums[n - i - 1 :] + nums[: n - i - 1]
            is_sorted = True
            for j in range(1, n):
                if a[j] < a[j - 1]:
                    is_sorted = False
                    break
            if is_sorted:
                return i + 1
        return -1

print(Solution().minimumRightShifts([3,4,5,1,2]))
print(Solution().minimumRightShifts([1,3,5]))
print(Solution().minimumRightShifts([2,1,4]))
