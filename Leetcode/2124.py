class Solution:
    def checkString(self, s: str) -> bool:
        if len(set(s)) == 1:
            return True
        ma = 0
        mb = 10**5
        for i in range(len(s)):
            if s[i] == "a" and ma < i:
                ma = i
            elif s[i] == "b" and mb > i:
                mb = i
        return ma < mb


print(Solution().checkString("aaabbb"))
print(Solution().checkString("abab"))
print(Solution().checkString("bbb"))
