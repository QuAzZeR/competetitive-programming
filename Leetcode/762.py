import math


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n == 2 or n == 3:
                return 1
            if n == 1:
                return 0
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return 0
            return 1

        answer = 0
        for i in range(left, right + 1):
            answer += is_prime(bin(i).count("1"))
        return answer


print(Solution().countPrimeSetBits(6, 10))
print(Solution().countPrimeSetBits(10, 15))
