from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] +=1
        answer = sum(filter(lambda x: d[x] == 1, d))
        return answer


print(Solution().sumOfUnique([1,2,3,2]))
print(Solution().sumOfUnique([1,1,1,1,1]))
print(Solution().sumOfUnique([1,2,3,4,5]))
