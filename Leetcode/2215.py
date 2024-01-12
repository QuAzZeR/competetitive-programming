from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)
        answer1 = []
        answer2 = []
        for i in n1:
            if i not in n2:
                answer1.append(i)
        for i in n2:
            if i not in n1:
                answer2.append(i)
        return [answer1, answer2]
print(Solution().findDifference([1,2,3],[2,4,6]))
print(Solution().findDifference([1,2,3,3], [1,1,2,2]))
