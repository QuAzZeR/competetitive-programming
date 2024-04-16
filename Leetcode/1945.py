class Solution:
    def getLucky(self, s: str, k: int) -> int:
        val = "".join([str(ord(i) - 96) for i in s])
        for _ in range(k):
            val = str(sum([int(i) for i in val]))
        return int(val)


print(Solution().getLucky("iiii", 1))
print(Solution().getLucky("leetcode", 2))
