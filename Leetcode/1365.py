from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            count = 0 
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            answer.append(count)
        return answer
print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))
print(Solution().smallerNumbersThanCurrent([6,5,4,8]))
print(Solution().smallerNumbersThanCurrent([7,7,7,7]))
