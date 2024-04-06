class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        p_count = 0
        new_s = list(s)
        for i in range(len(new_s)):
            if new_s[i] == ")":
                if p_count == 0:
                    new_s[i] = "*"
                else:
                    p_count -= 1
            elif new_s[i] == "(":
                p_count += 1
        for i in range(len(new_s) - 1, -1, -1):
            if p_count > 0 and new_s[i] == "(":
                new_s[i] = "*"
                p_count -= 1
        return "".join([i for i in new_s if i != "*"])


print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
print(Solution().minRemoveToMakeValid("a)b(c)d"))
print(Solution().minRemoveToMakeValid("))(("))
