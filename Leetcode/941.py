from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        is_increased = True
        m = max(arr)
        if m == arr[0] or m == arr[-1]:
            return False
        for i in range(0, n - 1):
            if arr[i] == m:
                is_increased = False
            if is_increased and arr[i] >= arr[i + 1]:
                return False
            elif (not is_increased) and arr[i] <= arr[i + 1]:
                return False

        return not is_increased


print(Solution().validMountainArray([2, 1]))
print(Solution().validMountainArray([3, 5, 5]))
print(Solution().validMountainArray([0, 3, 2, 1]))
print(Solution().validMountainArray([0, 2, 3, 4, 5, 2, 1, 0]))
print(Solution().validMountainArray([0, 2, 3, 3, 5, 2, 1, 0]))
print(Solution().validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
