class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        for i in range(len(s)):
            if s[i] =='6':
                s[i] = '9'
                break
        return int(''.join(s))

print(Solution().maximum69Number(9669))
print(Solution().maximum69Number(9996))
print(Solution().maximum69Number(9999))
