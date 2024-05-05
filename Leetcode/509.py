class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        if n < 2:
            return f[n]
        for i in range(2, n + 1):
            f.append(f[i - 1] + f[i - 2])
        return f[-1]


print(Solution().fib(2))
print(Solution().fib(3))
print(Solution().fib(4))
