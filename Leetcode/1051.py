from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected  = sorted(heights)
        answer = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                answer +=1
        return answer

print(Solution().heightChecker([1,1,4,2,1,3]))
print(Solution().heightChecker([5,1,2,3,4]))
print(Solution().heightChecker([1,2,3,4,5]))
