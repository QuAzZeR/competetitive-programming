class Solution:
    def minimumSum(self, num: int) -> int:
        digit = [int(i) for i in str(num)] 
        digit = sorted(digit)
        num1 = digit[0]*10 + digit[2] 
        num2 = digit[1]*10 + digit[3] 
        return num1 + num2
print(Solution().minimumSum(2932))
print(Solution().minimumSum(4009))
