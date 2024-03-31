from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        groups = []
        start = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                end = i - 1
                groups.append([start, end])
                start = i
        groups.append([start, len(s) - 1])

        return [i for i in groups if i[1] - i[0] >= 2]


print(Solution().largeGroupPositions("abbxxxxzzy"))
print(Solution().largeGroupPositions("abc"))
print(Solution().largeGroupPositions("abcdddeeeeaabbbcd"))
