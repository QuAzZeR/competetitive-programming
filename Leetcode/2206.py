from typing import Counter, List
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for i in d:
            if d[i]%2 != 0:
                return False

        return True
print(Solution().divideArray([3,3,2,2,2,2]))
print(Solution().divideArray([1,2,3,4]))
