from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        answer = [0] * n
        times = [0] * n
        meetings.sort()
        for start, end in meetings:
            m = -1
            f = False
            val = float("inf")
            for j in range(n):
                if times[j] < val:
                    val = times[j]
                    m = j
                if times[j] <= start:
                    f = True
                    answer[j] += 1
                    times[j] = end
                    break
            if not f:
                answer[m] += 1
                times[m] += end - start
        m = -1
        room = 0
        for i in range(n):
            if answer[i] > m:
                m = answer[i]
                room = i
        return room


print(Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))
print(Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))
