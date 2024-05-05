class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        ch = False
        v = False
        c = False
        sp = False
        for i in word:
            if i >= "0" and i <= "9":
                ch = True
            elif (
                (i >= "a" and i <= "z") or (i >= "A" and i <= "Z")
            ) and i.lower() not in ["a", "e", "i", "o", "u"]:
                c = True
                ch = True
            elif i.lower() in ["a", "e", "i", "o", "u"]:
                v = True
                ch = True
            else:
                sp = True
        return ch and v and c and not sp


print(Solution().isValid("234Adas"))
print(Solution().isValid("b3"))
print(Solution().isValid("a3$e"))
