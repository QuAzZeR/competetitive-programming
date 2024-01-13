from typing import List
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = [min(nums), max(nums)]
        answer = 1
        for i in range(2, a[-1]+1):
            if a[0]%i == 0 and a[1]%i == 0:
                answer = i
        return answer
print(Solution().findGCD([2,5,6,9,10]))
print(Solution().findGCD([7,5,6,8,3]))
print(Solution().findGCD([3,3]))
