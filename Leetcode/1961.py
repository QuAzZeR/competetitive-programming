from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        t = ""
        for i in words:
            t += i
            if t == s:
                return True

            if len(t) >= len(s):
                return False
        return False


print(Solution().isPrefixString("iloveleetcode", ["i", "love", "leetcode", "apples"]))
print(Solution().isPrefixString("iloveleetcode", ["apples", "i", "love", "leetcode"]))
