class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n <= 2:
            return t[n]
        for i in range(3, n + 1):
            v = t[i - 1] + t[i - 2] + t[i - 3]
            t.append(v)
        return t[-1]


print(Solution().tribonacci(4))
print(Solution().tribonacci(25))
