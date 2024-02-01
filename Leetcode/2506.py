from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        answer = 0
        l = len(words)
        for i in range(l - 1):
            for j in range(i + 1, l):
                if set(words[i]) == set(words[j]):
                    answer += 1
        return answer


print(Solution().similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]))
print(Solution().similarPairs(["aabb", "ab", "ba"]))
print(Solution().similarPairs(["nba", "cba", "dba"]))
