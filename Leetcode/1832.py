class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        answer = True
        char = {chr(i):0 for i in range(97,123)}
        for i in sentence:
            char[i] += 1
        return sum([1 for i in char if char[i] >= 1]) == 26

print(Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(Solution().checkIfPangram("leetcode"))
