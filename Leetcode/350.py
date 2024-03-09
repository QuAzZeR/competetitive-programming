from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        answer = []
        for i in d1:
            if i in d2:
                answer += [i] * (min(d1[i], d2[i]))
        return answer


print(Solution().intersect([1, 2, 2, 1], [2, 2]))
print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))
