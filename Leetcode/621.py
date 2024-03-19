from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        frequency = sorted(d.values())
        works_count = sum(frequency)
        current = frequency[-1] - 1
        idles = current * n
        for i in range(len(frequency) - 2, -1, -1):
            idles -= min(current, frequency[i])
        return (works_count + idles) if idles >= 0 else works_count


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(Solution().leastInterval(["A", "C", "A", "B", "D", "B"], 1))
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 3))
