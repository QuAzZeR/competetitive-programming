class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for word in text.split(' '):
            can_type = True
            for j in brokenLetters:
                if j in word:
                    can_type = False
                    break
            if can_type:
                count += 1
        return count
print(Solution().canBeTypedWords(text = "hello world", brokenLetters = "ad"))
print(Solution().canBeTypedWords(text = "leet code", brokenLetters = "lt"))
print(Solution().canBeTypedWords(text = "leet code", brokenLetters = "e"))
