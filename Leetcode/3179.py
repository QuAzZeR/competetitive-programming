class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        a = [1] * n
        for i in range(k):
            for j in range(1, n):
                a[j] = (a[j] + a[j - 1]) % mod
        return a[-1]


print(Solution().valueAfterKSeconds(4, 5))
print(Solution().valueAfterKSeconds(5, 3))
