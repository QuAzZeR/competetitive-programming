from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {arr2[i]: i for i in range(len(arr2))}
        return sorted([i for i in arr1 if i in d], key=lambda x: (d[x], x)) + sorted(
            [i for i in arr1 if i not in d]
        )


print(
    Solution().relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])
)
print(Solution().relativeSortArray([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))
