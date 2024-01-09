from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            for j in word:
                if j not in allowed:
                    count += 1
                    break
        return len(words) - count

print(Solution().countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
print(Solution().countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
print(Solution().countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))
