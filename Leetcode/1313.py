from typing import List
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0, len(nums), 2):
            answer += [nums[i+1]]*nums[i]
        return answer
print(Solution().decompressRLElist([1,2,3,4]))
print(Solution().decompressRLElist([1,1,2,3]))
