from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        answer = []
        for i in range(1,len(mountain)-1):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                answer.append(i)
        return answer

print(Solution().findPeaks([2,4,4]))
print(Solution().findPeaks([1,4,3,8,5]))
