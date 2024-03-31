class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = sum([int(i) for i in str(x)])
        if x % s == 0:
            return s
        return -1


print(Solution().sumOfTheDigitsOfHarshadNumber(18))
print(Solution().sumOfTheDigitsOfHarshadNumber(23))
