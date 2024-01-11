class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = len(s)
        copy = s[::-1]
        answer = ''
        for i in range(l):
            answer += min(copy[i],s[i])
        return answer

print(Solution().makeSmallestPalindrome("egcfe"))
print(Solution().makeSmallestPalindrome("abcd"))
print(Solution().makeSmallestPalindrome("seven"))
print(Solution().makeSmallestPalindrome("atie"))
