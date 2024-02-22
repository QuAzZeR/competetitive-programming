from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        answer = 0
        tt = {}
        pp = {}
        if len(trust) == 0:
            if n == 1:
                return 1
            return -1
        for p, t in trust:
            if t not in tt:
                tt[t] = 0
            tt[t] += 1
            if p not in pp:
                pp[p] = 0
            pp[p] += 1
        for i in range(1, n + 1):
            answer = True
            if i in tt:
                answer = answer and (tt[i] == n - 1)
            if i not in tt:
                answer = False
            if i in pp:
                answer = False
            if answer is True:
                return i

        return -1


print(Solution().findJudge(2, [[1, 2]]))
print(Solution().findJudge(3, [[1, 3], [2, 3]]))
print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]))
print(Solution().findJudge(2, []))
print(Solution().findJudge(1, []))
print(
    Solution().findJudge(
        11,
        [
            [1, 8],
            [1, 3],
            [2, 8],
            [2, 3],
            [4, 8],
            [4, 3],
            [5, 8],
            [5, 3],
            [6, 8],
            [6, 3],
            [7, 8],
            [7, 3],
            [9, 8],
            [9, 3],
            [11, 8],
            [11, 3],
        ],
    )
)
