import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        new_p = p[0]
        previous = p[0]
        
        for i in range(1,len(p)):
            if previous == '*' and p[i] == '*':
                continue
            new_p += p[i]
            previous = p[i]
        answer = re.match(r'^{0}$'.format(new_p), s)
        return answer is not None

print(Solution().isMatch("aa", "a"))
print(Solution().isMatch("aa", "a*"))
print(Solution().isMatch("aa", "a."))
print(Solution().isMatch("abc", "a***abc"))
