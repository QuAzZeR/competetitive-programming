from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        answer = -1
        d = {}
        for i in nums:
            m = int(max(list(str(i))))
            if i not in d:
                d[i] = m
        n = len(nums)
        for i in range(n - 1):
            n1 = nums[i]
            for j in range(i + 1, n):
                n2 = nums[j]
                if d[n1] == d[n2]:
                    answer = max(answer, n1 + n2)

        return answer


print(Solution().maxSum([51, 71, 17, 24, 42]))
print(Solution().maxSum([1, 2, 3, 4]))
