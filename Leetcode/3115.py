from typing import List
from math import isqrt


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        n = max(nums) + 1

        def get_primes():
            primes = [True] * (n + 1)
            primes[0] = False
            primes[1] = False
            for i in range(2, isqrt(n) + 1):
                if primes[i]:
                    for j in range(i * i, n, i):
                        primes[j] = False
            return primes

        primes = get_primes()
        d = {}
        for i in range(len(nums)):
            v = nums[i]
            if v not in d:
                d[v] = []
            d[v].append(i)
        min_index = 10**9
        max_index = -1
        for i in range(2, n + 1):
            if primes[i] and i in d:
                min_index = min([min_index] + d[i])
                max_index = max([max_index] + d[i])
        return abs(min_index - max_index)


print(Solution().maximumPrimeDifference([4, 2, 9, 5, 3]))
print(Solution().maximumPrimeDifference([4, 8, 2, 8]))
