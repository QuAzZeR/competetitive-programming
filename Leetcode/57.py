from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        answer = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            answer.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(intervals[i][1], newInterval[1]),
            ]
            i += 1
        answer.append(newInterval)
        while i < len(intervals):
            answer.append(intervals[i])
            i += 1
        return answer


print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
