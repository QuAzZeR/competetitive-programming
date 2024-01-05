from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and m[i] < m[j] + 1:
                    m[i] = m[j] + 1
            pass

        return max(m)

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS([0,1,0,3,2,3]))
print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))


