from typing import List
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        answer = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) <= nums[i]:
                    answer = max(answer, nums[i] ^ nums[j])
        return answer

print(Solution().maximumStrongPairXor([1,2,3,4,5]))
print(Solution().maximumStrongPairXor([10,100]))
print(Solution().maximumStrongPairXor([5,6,25,30]))
