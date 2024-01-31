from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1 = Counter(words1)
        d2 = Counter(words2)
        s = set(words1 + words2)
        answer = 0
        for i in s:
            if i in d1 and i in d2 and d1[i] == 1 and d2[i] == 1:
                answer += 1
        return answer


print(
    Solution().countWords(
        ["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"]
    )
)
print(Solution().countWords(["b", "bb", "bbb"], ["a", "aa", "aaa"]))
print(Solution().countWords(["a", "ab"], ["a", "a", "a", "ab"]))
