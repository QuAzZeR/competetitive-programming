from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        max_rob = [i for i in nums]
        n = len(nums)
        for i in range(1, n):
            m = max_rob[i]
            for j in range(i-1):
                m = max(m, max_rob[j] + max_rob[i])
            max_rob[i] = max([m, max_rob[i], max_rob[i-1]])

        return max_rob[-1]

print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))
