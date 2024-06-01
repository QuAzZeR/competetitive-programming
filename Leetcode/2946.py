from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        m = len(mat)
        c = mat
        if k % n == 0:
            return True
        for _ in range(k % n):
            new_mat = []
            for i in range(m):
                t = []
                if i % 2 == 0:
                    for j in range(1, n):
                        t.append(mat[i][j])
                    t.append(mat[i][0])
                else:
                    t.append(mat[i][-1])
                    for j in range(0, n - 1):
                        t.append(mat[i][j])
                new_mat.append(t)
            mat = new_mat
        for i in range(m):
            for j in range(n):
                if mat[i][j] != c[i][j]:
                    return False

        return True


print(Solution().areSimilar([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4))
print(Solution().areSimilar([[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], 2))
print(Solution().areSimilar([[2, 2], [2, 2]], 3))
