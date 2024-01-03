from typing import List
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        filters = list(filter(lambda x: x >= target, hours))
        return len(filters)
print(Solution().numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))
print(Solution().numberOfEmployeesWhoMetTarget([5,1,4,2,2], 6))
