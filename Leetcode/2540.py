from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = list(set(nums1).intersection(set(nums2)))
        if len(common) == 0:
            return -1
        return sorted(common)[0]


print(Solution().getCommon([1, 2, 3], [2, 4]))
print(Solution().getCommon([1, 2, 3, 6], [2, 3, 4, 5]))
