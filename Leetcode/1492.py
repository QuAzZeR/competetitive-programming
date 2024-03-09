class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        answer = -1
        c = 0
        for i in range(1, n + 1):
            if n % i == 0:
                c += 1
            if c == k:
                return i

        return answer


print(Solution().kthFactor(12, 3))
print(Solution().kthFactor(7, 2))
print(Solution().kthFactor(4, 4))
