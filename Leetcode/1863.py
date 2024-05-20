from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.answer = sum(nums)
        n = len(nums)

        def permu(expected, count, index, value):
            if count == expected:
                self.answer += value
                return
            for i in range(index, n):
                permu(expected, count + 1, i + 1, value ^ nums[i])

        for i in range(2, n + 1):
            permu(i, 0, 0, 0)
        return self.answer


print(Solution().subsetXORSum([1, 3]))
print(Solution().subsetXORSum([5, 1, 6]))
print(Solution().subsetXORSum([3, 4, 5, 6, 7, 8]))
