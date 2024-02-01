from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if nums.count(0) > 0:
            return 0

        return -1 if sum([1 for i in nums if i < 0]) % 2 else 1


print(Solution().arraySign([-1, -2, -3, -4, 3, 2, 1]))
print(Solution().arraySign([1, 5, 0, 2, -3]))
print(Solution().arraySign([-1, 1, -1, 1, -1]))
