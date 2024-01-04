from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    answer.append((i,j))
        return len(answer)


print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
print(Solution().numIdenticalPairs([1,1,1,1]))
print(Solution().numIdenticalPairs([1,2,3]))
