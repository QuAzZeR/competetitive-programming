class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num[-1]) % 2 != 0:
            return num
        n = len(num)
        for i in range(n - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[0 : i + 1]
        return ""


print(Solution().largestOddNumber("52"))
print(Solution().largestOddNumber("4206"))
print(Solution().largestOddNumber("35427"))
print(Solution().largestOddNumber("35472"))
