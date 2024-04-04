from typing import List
from math import isqrt


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
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
        answer = []
        for i in range(n // 2 + 1):
            if primes[i] and primes[n - i]:
                answer.append([i, n - i])

        return answer


print(Solution().findPrimePairs(10))
print(Solution().findPrimePairs(2))
print(Solution().findPrimePairs(999853))
print(Solution().findPrimePairs(5))
print(Solution().findPrimePairs(25))
print(Solution().findPrimePairs(6))
