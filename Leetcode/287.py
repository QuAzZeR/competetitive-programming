from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        answer = 0
        d = {}
        for num in nums:
            if num in d:
                return num
            d[num] = 0
        return answer


print(Solution().findDuplicate([1, 3, 4, 2, 2]))
print(Solution().findDuplicate([3, 1, 3, 4, 2]))
print(Solution().findDuplicate([3, 3, 3, 3, 3]))
