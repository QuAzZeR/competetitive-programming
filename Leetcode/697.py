from typing import List
from collections import Counter, defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = Counter(nums)
        m = max(d.values())
        n = len(nums)
        answer = n
        l = 0
        r = 0
        freq = defaultdict(int)
        while l <= r and r < n:
            freq[nums[r]] += 1
            if freq[nums[r]] == m:
                while nums[r] != nums[l]:
                    freq[nums[l]] -= 1
                    l += 1
                answer = min(answer, r - l + 1)
            r += 1
        return answer


print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
print(Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
