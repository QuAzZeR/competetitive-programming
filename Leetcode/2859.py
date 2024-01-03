from typing import List
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(len(nums)):
            is_bit_correct = sum([int(j) for j in bin(i).split('b')[-1]])
            if is_bit_correct == k:
                answer += nums[i]
        return answer
        
print (Solution().sumIndicesWithKSetBits([5,10,1,5,2], 1))
print (Solution().sumIndicesWithKSetBits([4,3,2,1], 2))
