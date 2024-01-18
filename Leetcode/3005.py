from typing import Counter, List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = dict(Counter(nums))
        m = max(d.values())
        return sum([d[i] for i in d if d[i] == m])
print(Solution().maxFrequencyElements([1,2,2,3,1,4]))
print(Solution().maxFrequencyElements([1,2,3,4,5]))
