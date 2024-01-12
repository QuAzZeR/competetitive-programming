class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)
        a = s[:l//2].lower()
        b = s[l//2:].lower()
        vowel = ['a', 'e','i','o','u']
        ca = 0
        cb = 0
        for i in range(l//2):
            if a[i] in vowel:
                ca +=1
            if b[i] in vowel:
                cb += 1
        return ca == cb

print(Solution().halvesAreAlike("book"))
print(Solution().halvesAreAlike("textbook"))
