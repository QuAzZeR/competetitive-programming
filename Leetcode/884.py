from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        answer = []
        d1 = Counter(s1.split(" "))
        d2 = Counter(s2.split(" "))
        u1 = set([i for i in d1 if d1[i] == 1])
        u2 = set([i for i in d2 if d2[i] == 1])
        w1 = set(d1.keys())
        w2 = set(d2.keys())
        answer += list(u1 - w2)
        answer += list(u2 - w1)
        return answer


print(Solution().uncommonFromSentences("this apple is sweet", "this apple is sour"))
print(Solution().uncommonFromSentences("apple apple", "banana"))
print(Solution().uncommonFromSentences("s z z z s", "s z ejt"))
