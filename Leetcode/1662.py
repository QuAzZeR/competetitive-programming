from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        return ''.join(word1) == ''.join(word2)

print(Solution().arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
print(Solution().arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
print(Solution().arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
