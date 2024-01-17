class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        m = {chr(i+97): str(i) for i in range(10)}
        word_1 = int(''.join([m[i] for i in firstWord]))
        word_2 = int(''.join([m[i] for i in secondWord]))
        word_t = int(''.join([m[i] for i in targetWord]))
        return word_1 + word_2 == word_t
print(Solution().isSumEqual(firstWord = "acb", secondWord = "cba", targetWord = "cdb"))
print(Solution().isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aab"))
print(Solution().isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aaaa"))
