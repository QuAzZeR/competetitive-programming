from typing import List
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        answer = []
        for i in nums:
            answer += list(range(i[0],i[1]+1))

        return len(set(answer))

print(Solution().numberOfPoints([[3,6], [1,5], [4,7]]))
print(Solution().numberOfPoints([[1,3],[5,8]]))
