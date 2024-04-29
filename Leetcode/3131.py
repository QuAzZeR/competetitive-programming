from typing import List
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        df = [nums2[i] - nums1[i] for i in range(len(nums1))]
        answer = sum(df) //len(df)

        return answer

print(Solution().addedInteger([2,6,4], [9,7,5]))
print(Solution().addedInteger([10], [5]))
print(Solution().addedInteger([1,1,1,1], [1,1,1,1]))