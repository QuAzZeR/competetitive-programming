from typing import Counter, List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        answer = [0,0]
        for i in range(1, len(nums)+1):
            if i not in d:
                answer[1] = i
                continue
            if d[i] == 2:
                answer[0] = i
        return answer



print(Solution().findErrorNums([1,2,2,4]))
print(Solution().findErrorNums([1,1]))
