class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        answer = 0
        d = {}
        for i in range(len(word)):
            w = word[i]
            if w not in d:
                d[w] = i
            if ord(w) < 97:
                continue
            d[w] = i
        s = set(word)
        s = set([i for i in s if ord(i) >= 97])
        for i in s:
            if i.upper() in d and d[i] < d[i.upper()]:
                answer += 1
        return answer


print(Solution().numberOfSpecialChars("aaAbcBC"))
print(Solution().numberOfSpecialChars("abc"))
print(Solution().numberOfSpecialChars("AbBCab"))
print(Solution().numberOfSpecialChars("cCceDC"))
