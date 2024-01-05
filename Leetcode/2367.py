from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        answer += 1

        return answer
print(Solution().arithmeticTriplets([0,1,4,6,7,10], 3))
print(Solution().arithmeticTriplets([4,5,6,7,8,9], 2))
