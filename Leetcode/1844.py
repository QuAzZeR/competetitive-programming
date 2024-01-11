class Solution:
    def replaceDigits(self, s: str) -> str:
        answer = ''
        for i in range(0, len(s)):
            if s[i] >= '0' and s[i] <= '9':
                answer += chr(ord(s[i-1])+int(s[i]))
            else:
                answer += s[i]

        return answer

print(Solution().replaceDigits('a1c1e1'))
print(Solution().replaceDigits('a1b2c3d4e'))
