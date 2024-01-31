from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        answer = True
        arr = sorted(arr)
        d = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if d != arr[i] - arr[i - 1]:
                answer = False
                break

        return answer


print(Solution().canMakeArithmeticProgression([3, 5, 1]))
print(Solution().canMakeArithmeticProgression([1, 2, 4]))
