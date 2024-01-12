class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        r = int(str(num)[::-1])
        return str(r)[::-1] == str(num)


print(Solution().isSameAfterReversals(526))
print(Solution().isSameAfterReversals(1800))
print(Solution().isSameAfterReversals(0))
