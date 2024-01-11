from typing import List
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        answer = 0
        l = len(batteryPercentages)
        for i in range(l):
            if batteryPercentages[i] <= 0:
                continue
            batteryPercentages[i] += 1
            for j in range(i+1,l):
                batteryPercentages[j] -= 1
            answer += 1
        return answer
print(Solution().countTestedDevices([1,1,2,1,3]))
print(Solution().countTestedDevices([0,1,2]))
