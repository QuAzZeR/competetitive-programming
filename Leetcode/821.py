from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l = len(s)
        answer = [0] * l
        cc = [i for i in range(l) if s[i] == c]
        for i in range(l):
            if s[i] == c:
                continue
            m = 10**9
            for j in cc:
                if m > abs(j - i):
                    m = abs(j - i)
            answer[i] = m

        return answer


print(Solution().shortestToChar("loveleetcode", "e"))
print(Solution().shortestToChar("aaab", "b"))
