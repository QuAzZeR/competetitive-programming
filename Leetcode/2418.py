from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [i[0] for i in sorted([(names[i], heights[i]) for i in range(len(names))], key=lambda x: -x[1])]

print(Solution().sortPeople(["Mary","John","Emma"], [180,165,170]))
print(Solution().sortPeople(["Alice","Bob","Bob"], heights = [155,185,150]))
