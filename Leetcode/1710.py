from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x: (-x[1], -x[0]))
        i = 0
        current_size = 0
        total_units = 0
        for i in range(len(boxTypes)):
            n, u = boxTypes[i]
            if current_size + n <= truckSize:
                current_size += n
                total_units += n*u
            else:
                remain = truckSize - current_size
                current_size += remain
                total_units += remain * u

            if current_size == truckSize:
                break

        return total_units

print(Solution().maximumUnits([[1,3],[2,2],[3,1]], 4))
print(Solution().maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))
