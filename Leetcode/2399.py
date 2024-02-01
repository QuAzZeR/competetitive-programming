from collections import defaultdict
from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = defaultdict(list)
        for i in range(len(s)):
            d[s[i]].append(i)
        for i in set(s):
            dist = distance[ord(i) - 97]
            diff = abs(d[i][0] - d[i][1]) - 1
            if diff != dist:
                return False
        return True


print(
    Solution().checkDistances(
        "abaccb",
        distance=[
            1,
            3,
            0,
            5,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
    )
)
print(
    Solution().checkDistances(
        "aa",
        distance=[
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
    )
)
print(
    Solution().checkDistances(
        "abcabc",
        [0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    )
)
