class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set([i.lower() for i in word])
        w = set(word)
        answer = 0
        for i in s:
            if i.upper() in w and i.lower() in w:
                answer += 1
        return answer


print(Solution().numberOfSpecialChars("aaAbcBC"))
print(Solution().numberOfSpecialChars("abc"))
print(Solution().numberOfSpecialChars("abBCab"))
