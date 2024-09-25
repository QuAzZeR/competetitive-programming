from typing import List
import unittest


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        answer = 0
        pre_map = {}
        for a in arr1:
            s = str(a)
            pre = ""
            for c in s:
                pre += c
                pre_map[pre] = pre_map.get(pre,0) +1
        for a in arr2:
            s = str(a)
            pre = ""
            for c in s:
                pre += c
                if pre in pre_map:
                    answer = max(answer, len(pre))
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix([1,10,100], [1000]), 3)
        self.assertEqual(s.longestCommonPrefix([1,2,3], [4,4,4]), 0)


if __name__ == "__main__":
    unittest.main()
