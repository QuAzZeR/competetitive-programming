from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        answer = 0

        for i in arr1:
            is_cal = True
            for j in arr2:
                if abs(i - j) <= d:
                    is_cal = False
                    break
            if is_cal:
                answer += 1

        return answer


print(Solution().findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))
print(Solution().findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3))
print(Solution().findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))
