from typing import List
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = []
        for i in arr:
            d.append((i, bin(i).count('1')))
        d = sorted(d, key=lambda x: (x[1],x[0]))
        return list(map(lambda x: x[0], d))

print(Solution().sortByBits([0,1,2,3,4,5,6,7,8]))
print(Solution().sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))
