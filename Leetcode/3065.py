from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        c = 0
        for i in nums:
            if i >= k:
                return c
            c += 1
        return 0


print(Solution().minOperations([2, 11, 10, 1, 3], 10))
print(Solution().minOperations([1, 1, 2, 4, 9], 1))
print(Solution().minOperations([1, 1, 2, 4, 9], 9))
