from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for i in range(1,n+1):
            answer.append(nums[i-1])
            answer.append(nums[n +i-1])
        return answer

print(Solution().shuffle([2,5,1,3,4,7],3))
print(Solution().shuffle([1,2,3,4,4,3,2,1],4))
print(Solution().shuffle([1,1,2,2], 2))


