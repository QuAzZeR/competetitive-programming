from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        n = len(meetings)
        merge_meetings = []
        answer = abs(meetings[0][0] - 1)
        for i in range(1, n):
            if meetings[i][0] <= meetings[i - 1][1]:
                if meetings[i][1] < meetings[i - 1][1]:
                    meetings[i][1] = meetings[i - 1][1]
            else:
                d = meetings[i][0] - meetings[i - 1][1]
                answer += d - 1
        answer += abs(meetings[-1][1] - days)
        return answer


print(Solution().countDays(10, [[5, 7], [1, 3], [9, 10]]))
print(Solution().countDays(5, [[2, 4], [1, 3]]))
print(Solution().countDays(6, [[1, 6]]))
