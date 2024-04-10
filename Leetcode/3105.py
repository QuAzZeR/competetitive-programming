from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        answer = 1
        n = len(nums)
        for i in range(n):
            c_d = 1
            c_i = 1
            for j in range(i + 1, n):
                if nums[j] > nums[j - 1]:
                    c_i += 1
                else:
                    break
            for j in range(i + 1, n):
                if nums[j] < nums[j - 1]:
                    c_d += 1
                else:
                    break
            answer = max([answer, c_i, c_d])
        return answer


print(Solution().longestMonotonicSubarray([1, 4, 3, 3, 2]))
print(Solution().longestMonotonicSubarray([3, 3, 3, 3]))
print(Solution().longestMonotonicSubarray([3, 2, 1]))
