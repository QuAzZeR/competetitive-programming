from typing import List
import unittest


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        self.pick = []
        n = len(candidates)
        candidates.sort()
        def combi(index, target):
            if target == 0:
                self.answer.append(self.pick[:])
                return
            for i in range(index,n ):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                self.pick.append(candidates[i])
                combi(i+1, target - candidates[i])
                self.pick.pop()
        combi(0, target)
        return self.answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.combinationSum2([10,1,2,7,6,1,5],8), [
[1,1,6],
[1,2,5],
[1,7],
[2,6]
])
        self.assertEqual(s.combinationSum2([2,5,2,1,2], 5), [
[1,2,2],
[5]
])


if __name__ == "__main__":
    unittest.main()
