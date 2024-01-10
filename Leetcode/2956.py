from typing import List
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = 0
        c2 = 0
        for i in nums1:
            if i in nums2:
                c1 += 1
        for i in nums2:
            if i in nums1:
                c2 += 1
        return [c1,c2]
print(Solution().findIntersectionValues([4,3,2,3,1], [2,2,5,2,3,6]))
print(Solution().findIntersectionValues([3,4,2,3], [1,5]))
