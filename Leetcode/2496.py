from typing import List
import re


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        m = 0
        for s in strs:
            l = 0
            if re.findall("\w", s):
                l = len(s)
            else:
                l = int(s)
            if m < l:
                m = l

        return m


print(Solution().maximumValue(["alic3", "bob", "3", "4", "00000"]))
print(Solution().maximumValue(["1", "01", "001", "0001"]))
print(
    Solution().maximumValue(["iw1", "61939", "7", "7i", "cye", "bv7yg", "t3ye6", "990"])
)
