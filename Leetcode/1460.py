from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)


print(Solution().canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))
print(Solution().canBeEqual([7], [7]))
print(Solution().canBeEqual([3, 7, 9], [3, 7, 11]))
