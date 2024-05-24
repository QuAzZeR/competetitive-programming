from typing import List
from collections import defaultdict


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.answer = n

        def dfs(index, d):
            if index == n:
                return 1

            taken = 0
            if d[nums[index] - k] == 0 and d[nums[index] + k] == 0:
                d[nums[index]] += 1
                taken = dfs(index + 1, d)
                d[nums[index]] -= 1

            not_taken = dfs(index + 1, d)
            return taken + not_taken

        d = defaultdict(int)
        return dfs(0, d) - 1


print(Solution().beautifulSubsets([2, 4, 6], 2))
print(Solution().beautifulSubsets([1], 1))
