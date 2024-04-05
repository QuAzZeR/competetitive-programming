from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 2:
            return True
        for i in range(n):
            new_l = nums[:i] + nums[i + 1 :]
            if sorted(new_l) == new_l:
                if len(set(new_l)) == n - 1:
                    return True

        return False


print(Solution().canBeIncreasing([1, 2, 10, 5, 7]))
print(Solution().canBeIncreasing([2, 3, 1, 2]))
print(Solution().canBeIncreasing([1, 1, 1]))
