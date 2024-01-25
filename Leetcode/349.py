from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        answer = []
        for i in nums1:
            if i in nums2:
                answer.append(i)

        for i in nums2:
            if i in nums1:
                answer.append(i)
        return list(set(answer))

print(Solution().intersection([1,2,2,1], [2,2]))
print(Solution().intersection([4,9,5], [9,4,9,8,4]))

