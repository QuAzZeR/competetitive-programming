from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque([("0000", 0)])
        visited = set("0000")
        while q:
            c, m = q.popleft()
            if c == target:
                return m
            for i in range(4):
                for j in [-1, 1]:
                    d = (int(c[i]) + j) % 10
                    nc = c[:i] + str(d) + c[i + 1 :]
                    if nc not in visited and nc not in deadends:
                        visited.add(nc)
                        q.append((nc, m + 1))

        return -1


print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
print(Solution().openLock(["8888"], target="0009"))
print(
    Solution().openLock(
        ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"
    )
)
