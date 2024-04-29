class Solution:
    def scoreOfString(self, s: str) -> int:
        answer = 0
        n = len(s)
        for i in range(n-1):
            answer += abs(ord(s[i]) - ord(s[i+1]))
        return answer

print(Solution().scoreOfString("hello"))
print(Solution().scoreOfString("zaz"))