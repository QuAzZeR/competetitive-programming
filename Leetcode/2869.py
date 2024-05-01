from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = nums[::-1]
        c = 0
        b = [0] * (k + 1)
        s = 0
        for i in nums:
            if i <= k:
                if b[i] == 0:
                    b[i] = 1
                    s += 1
            c += 1
            if s == k:
                break
        return c


print(Solution().minOperations([3, 1, 5, 4, 2], 2))
print(Solution().minOperations([3, 1, 5, 4, 2], 5))
print(Solution().minOperations([3, 2, 5, 3, 1], 3))
