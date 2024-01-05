from typing import List
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit = []
        for i in nums:
            digit += [int(d) for d in str(i)]
        digit_sum = sum(digit)
        return abs(element_sum - digit_sum)
print(Solution().differenceOfSum([1,15,6,3]))
print(Solution().differenceOfSum([1,2,3,4]))
