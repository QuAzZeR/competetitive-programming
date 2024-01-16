from collections import defaultdict
from typing import List
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        d = defaultdict(list)
        for i in set(nums1):
            d[i].append(1)
        for i in set(nums2):
            d[i].append(2)
        for i in set(nums3):
            d[i].append(3)

        return [i for i in d if len(d[i]) >= 2]

print(Solution().twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]))
print(Solution().twoOutOfThree(nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]))
print(Solution().twoOutOfThree(nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]))
