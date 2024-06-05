from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        intersect = Counter(words[0])
        for word in words[1:]:
            d = Counter(word)
            r = []
            for i in intersect:
                if i in d:
                    if d[i] < intersect[i]:
                        intersect[i] = d[i]
                else:
                    r.append(i)
            for i in r:
                del intersect[i]
        answer = []
        for i in intersect:
            answer += [i] * intersect[i]
        return answer


print(Solution().commonChars(["bella", "label", "roller"]))
print(Solution().commonChars(["cool", "lock", "cook"]))
