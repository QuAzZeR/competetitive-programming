from typing import Dict, List
def is_empty(d: Dict):
    return sum(d.values()) == 0

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        answer = []
        distinct_value = {}
        for i in nums:
            if i not in distinct_value:
                distinct_value[i] = 0
            distinct_value[i] += 1
        
        while not is_empty(distinct_value):
            current = []
            for i in distinct_value:
                if distinct_value[i] != 0:
                    current.append(i)
                    distinct_value[i] -= 1
            answer.append(current)

            
        return answer 
print(Solution().findMatrix([1,3,4,1,2,3,1]))
print(Solution().findMatrix([1,2,3,4]))
