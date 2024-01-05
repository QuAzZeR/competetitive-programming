from typing import List
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        answer = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if abs(nums[i] - nums[j]) ==k:
                    answer += 1
        return answer


print(Solution().countKDifference([1,2,2,1], 1))
print(Solution().countKDifference([1,3], 3))
print(Solution().countKDifference([3,2,1,5,4], 2))
