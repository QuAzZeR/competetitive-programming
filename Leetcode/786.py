from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        fraction = []
        for i in range(n):
            for j in range(i + 1, n):
                fraction.append(([arr[i], arr[j]], arr[i] / arr[j]))
        fraction.sort(key=lambda x: x[1])
        return fraction[k - 1][0]


print(Solution().kthSmallestPrimeFraction([1, 2, 3, 5], 3))
print(Solution().kthSmallestPrimeFraction([1, 7], 1))
