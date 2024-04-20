class Solution:
    def minOperations(self, s: str) -> int:
        l = len(s)
        first = "".join([str(i % 2) for i in range(l)])
        second = "".join([str(i % 2) for i in range(1, l + 1)])
        diff_first = bin(int(s, 2) ^ int(first, 2)).count("1")
        diff_second = bin(int(s, 2) ^ int(second, 2)).count("1")
        return min(diff_first, diff_second)


print(Solution().minOperations("0100"))
print(Solution().minOperations("10"))
print(Solution().minOperations("1111"))
