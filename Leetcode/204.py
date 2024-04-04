from typing import List
from math import isqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        def get_primes():
            primes = [True] * (n + 1)
            primes[0] = False
            primes[1] = False
            for i in range(2, isqrt(n) + 1):
                if primes[i]:
                    for j in range(i * i, n, i):
                        primes[j] = False
            return primes

        if n <= 1:
            return 0
        primes = get_primes()
        answer = 0
        for i in range(n):
            if primes[i]:
                answer += 1

        return answer


print(Solution().countPrimes(10))
print(Solution().countPrimes(0))
print(Solution().countPrimes(1))
