class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        h = n // 2 + int(n % 2)
        if n == 1:
            return False
        for i in range(h):
            new_s = s[0 : i + 1]
            len_new_s = len(new_s)
            if new_s * (n // len_new_s) == s:
                return True
        return False


print(Solution().repeatedSubstringPattern("abab"))
print(Solution().repeatedSubstringPattern("abc"))
print(Solution().repeatedSubstringPattern("abcabcabcabc"))
print(Solution().repeatedSubstringPattern("abcabcabcabc"))
