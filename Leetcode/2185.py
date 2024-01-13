from typing import List
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answer = 0
        l = len(pref)
        for i in words:
            if len(i) < l:
                continue
            if i[:l] == pref:
                answer += 1
        return answer
print(Solution().prefixCount(["pay","attention","practice","attend"], "at"))
print(Solution().prefixCount(["leetcode","win","loops","success"], "code"))

