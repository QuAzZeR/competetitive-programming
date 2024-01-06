from typing import List
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        answer = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                answer = sum(nums[0:i])
                break
        if answer == 0:
            answer = sum(nums)
        nums = sorted(nums)
        for i in range(0, len(nums)):
            if answer == nums[i]:
                answer += 1
            elif answer > nums[i]:
                continue
            elif answer < nums[i]:
                break

        return answer


print(Solution().missingInteger([1,2,3,2,5]))
print(Solution().missingInteger([3,4,5,1,12,14,13]))
print(Solution().missingInteger([29,30,31,32,33,34,35,36,37]))
print(Solution().missingInteger([38]))
