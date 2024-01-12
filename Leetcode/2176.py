from typing import List
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        l = len(nums)
        answer = 0
        for i in range(l):
            for j in range(i+1, l):
                if (i*j)%k == 0 and nums[i] == nums[j]:
                    answer += 1

        return answer
print(Solution().countPairs([3,1,2,2,2,1,3], 2))
print(Solution().countPairs([1,2,3,4], 1))
