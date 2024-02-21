class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        c = 0
        while left != right:
            left >>= 1
            right >>= 1
            c += 1
        return left << c


print(Solution().rangeBitwiseAnd(5, 7))
print(Solution().rangeBitwiseAnd(0, 0))
print(Solution().rangeBitwiseAnd(1, 2147483647))
