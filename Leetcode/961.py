from typing import Counter, List
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        d = Counter(nums)
        for i in d:
            if d[i] == n:
                return i

        return 0

print(Solution().repeatedNTimes([1,2,3,3]))
print(Solution().repeatedNTimes([2,1,2,5,3,2]))
print(Solution().repeatedNTimes([5,1,5,2,5,3,5,4]))
