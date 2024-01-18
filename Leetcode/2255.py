from typing import List
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        ls = len(s)
        for word in words:
            l = len(word)
            if l > ls:
                continue
            if word == s[:l]:
                count += 1

        return count


print(Solution().countPrefixes(words = ["a","b","c","ab","bc","abc"], s = "abc"))
print(Solution().countPrefixes(words = ["a","a"], s = "aa"))
