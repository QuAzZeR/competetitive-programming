class Solution:
    def convertToBase7(self, num: int) -> str:
        answer = ""
        if num == 0:
            return "0"
        minus = True if num < 0 else False
        num = abs(num)
        while num >= 1:
            answer += str(num % 7)
            num //= 7
        return ("-" if minus else "") + answer[::-1]


print(Solution().convertToBase7(100))
print(Solution().convertToBase7(-7))
print(Solution().convertToBase7(0))
