from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive = 0
        negative = 0
        for i in nums:
            if i > 0:
                positive += 1
            elif i < 0:
                negative += 1
        return max(positive, negative)


print(Solution().maximumCount([-2, -1, -1, 1, 2, 3]))
print(Solution().maximumCount([-3, -2, -1, 0, 0, 1, 2]))
print(Solution().maximumCount([5, 20, 66, 1314]))
