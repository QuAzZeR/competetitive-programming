from typing import List
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        m = 1000
        for i in range(len(nums)):
            if i%10 == nums[i]:
                m = i
                break
        if m == 1000:
            return -1
        return  m

print(Solution().smallestEqual([0,1,2]))
print(Solution().smallestEqual([4,3,2,1]))
print(Solution().smallestEqual([1,2,3,4,5,6,7,8,9,0]))
