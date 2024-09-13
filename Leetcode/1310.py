from typing import List
import unittest


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] ^ arr[i]
        answer = []
        for l,r in queries:
            if l == 0:
                answer.append(prefix[r])
            else:
                answer.append(prefix[r] ^ prefix[l-1])
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]), [2,7,14,8] )
        self.assertEqual(s.xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]), [8,0,4,4])


if __name__ == "__main__":
    unittest.main()
