from typing import List
import functools
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        new_nums = [ i for i in nums if i != 0]
        if len(new_nums) == 0:
            return [0]*len(nums)
        if len(new_nums) < len(nums)-1 and len(nums) != 1:
            return [0]*len(nums)
        result = functools.reduce(lambda a,b: a*b, new_nums)
        zero = 0 in nums
        for i in nums:
            if zero:
                if i == 0:
                    answer.append(result)
                else:
                    answer.append(0)
            else:
                answer.append(result//i)
        return answer
print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf([-1,1,0,-3,3]))
print(Solution().productExceptSelf([0,0]))
print(Solution().productExceptSelf([0,4,0]))
print(Solution().productExceptSelf([0,1]))
