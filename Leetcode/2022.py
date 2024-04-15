from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        matrix = []
        l = len(original)
        if m * n != l:
            return matrix
        c = 0
        for i in range(m):
            s = []
            for j in range(n):
                s.append(original[c])
                c += 1
            matrix.append(s)
        return matrix


print(Solution().construct2DArray([1, 2, 3, 4], 2, 2))
print(Solution().construct2DArray([1, 2, 3, 4, 5, 6], 2, 3))
print(Solution().construct2DArray([1, 2, 3, 4, 5, 6], 3, 2))
print(Solution().construct2DArray([1, 2, 3], 1, 3))
print(Solution().construct2DArray([1, 2, 3], 1, 1))
