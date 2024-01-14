from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = [i for i in nums if i%2 == 0]
        odd = [i for i in nums if i%2 != 0]

        return even + odd

print(Solution().sortArrayByParity([3,1,2,4]))
print(Solution().sortArrayByParity([0]))
