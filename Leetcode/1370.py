from typing import Counter


class Solution:
    def sortString(self, s: str) -> str:
        answer = ''
        d = dict(Counter(s))
        ss = sorted(list(set(s)))
        current = 0
        ls = len(s)
        lss = len(ss)
        direction = 1
        while len(answer) < ls:
            c = ss[current]
            current += direction
            if d[c] > 0:
                answer += c
                d[c] -= 1
            if current > lss-1:
                direction = -1
                current = lss-1
            if current < 0:
                direction = 1
                current = 0
        return answer
print(Solution().sortString('aaaabbbbcccc'))
print(Solution().sortString('leetcode'))
print(Solution().sortString('rat'))
