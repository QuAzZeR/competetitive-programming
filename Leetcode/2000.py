class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        sub = word.find(ch)
        if sub == -1:
            return word
        return word[sub::-1] + word[sub+1:]
print(Solution().reversePrefix("abcdefd","d"))
print(Solution().reversePrefix("xyxzxe","z"))
print(Solution().reversePrefix("abcd","z"))
