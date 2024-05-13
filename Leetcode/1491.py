from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        n = len(salary)
        answer = sum(salary[1 : n - 1]) / (n - 2)
        return answer


print(Solution().average([4000, 3000, 1000, 2000]))
print(Solution().average([3000, 1000, 2000]))
