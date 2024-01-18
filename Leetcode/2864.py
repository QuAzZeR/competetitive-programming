class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        x = s.count('1')
        n = len(s)
        return "{0}{1}".format('1'*(x-1), '0'*(n-x)) + '1'
print(Solution().maximumOddBinaryNumber("010"))
print(Solution().maximumOddBinaryNumber("0101"))
print(Solution().maximumOddBinaryNumber("00111"))
