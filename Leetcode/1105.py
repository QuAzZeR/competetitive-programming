from typing import List
import unittest


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        f = [0] *(n+1)
        for i in range(1,n+1):
            w,h = books[i-1]
            f[i] = f[i-1] + h
            for j in range(i-1, 0, -1):
                w += books[j-1][0]
                if w > shelfWidth:
                    break
                h = max(h, books[j-1][1])
                f[i] = min(f[i], f[j-1] + h)
        return f[n]


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4), 6)
        self.assertEqual(s.minHeightShelves([[1,3],[2,4],[3,2]], 6), 4)


if __name__ == "__main__":
    unittest.main()
