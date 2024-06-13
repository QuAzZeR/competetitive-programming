class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        for i in range(0, n - 1):
            if words[i + 1][0] != words[i][-1]:
                return False
        if words[-1][-1] != words[0][0]:
            return False
        return True


print(Solution().isCircularSentence("leetcode exercises sound delightful"))
print(Solution().isCircularSentence("eetcode"))
print(Solution().isCircularSentence("Leetcode is cool"))
print(Solution().isCircularSentence("ab a"))
