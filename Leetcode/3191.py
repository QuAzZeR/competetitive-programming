from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        self.answer = 0
        n = len(nums)

        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = int(not nums[i + 1])
                nums[i + 2] = int(not nums[i + 2])
                self.answer += 1

        return self.answer if sum(nums) == n else -1


print(Solution().minOperations([0, 1, 1, 1, 0, 0]))
print(Solution().minOperations([0, 1, 1, 1]))
print(
    Solution().minOperations([0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1])
)
