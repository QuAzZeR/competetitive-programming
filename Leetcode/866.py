from typing import List
from math import isqrt


class Solution:
    def primePalindrome(self, n: int) -> int:
        power = min(len(str(n)) + 2, 8)
        m = 2 * 10**power

        def get_primes():
            primes = [True] * (m + 1)
            primes[0] = False
            primes[1] = False
            for i in range(2, isqrt(m) + 1):
                if primes[i]:
                    for j in range(i * i, m, i):
                        primes[j] = False
            return primes

        primes = get_primes()
        answer = 0
        for i in range(n, m + 1):
            if primes[i] and str(i) == "".join(str(i)[::-1]):
                return i

        return answer


print(Solution().primePalindrome(6))
print(Solution().primePalindrome(8))
print(Solution().primePalindrome(13))
