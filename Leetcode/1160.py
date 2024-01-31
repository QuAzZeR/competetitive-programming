from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        answer = 0
        d = Counter(chars)
        for i in words:
            c = Counter(i)
            is_exist = True
            for j in c:
                if j not in d:
                    is_exist = False
                    break
                if d[j] < c[j]:
                    is_exist = False
                    break

            if is_exist:
                answer += len(i)
        return answer


print(Solution().countCharacters(["cat", "bt", "hat", "tree"], "atach"))
print(Solution().countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))
