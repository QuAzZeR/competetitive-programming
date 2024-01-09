from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]
        for i in gain:
            altitude.append(altitude[-1] + i)
        return sorted(altitude,reverse=True)[0]

print(Solution().largestAltitude([-5,1,5,0,-7]))
print(Solution().largestAltitude([-4,-3,-2,-1,4,3,2]))
