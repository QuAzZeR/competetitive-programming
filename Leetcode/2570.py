from collections import defaultdict
from typing import List
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for x,y in nums1:
            d[x] += y
        for x,y in nums2:
            d[x] += y
        return sorted([[i,d[i]] for i in d], key=lambda x: x[0])

print(Solution().mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]))
print(Solution().mergeArrays(nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]))
