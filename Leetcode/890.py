from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        answer = []
        for word in words:
            m = {}
            reverse_m = {}
            is_pattern = True
            for i in range(len(word)):
                c = word[i]
                p = pattern[i]
                print(m, reverse_m)
                if p in reverse_m:
                    if reverse_m[p] != c:
                        is_pattern = False
                        break
                if c not in m:
                    m[c] = p
                    reverse_m[p] = c
                elif m[c] != pattern[i]:
                    is_pattern = False
                    break
            if is_pattern:
                answer.append(word)

        return answer


print(
    Solution().findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb")
)
print(Solution().findAndReplacePattern(["a", "b", "c"], pattern="a"))
