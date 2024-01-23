from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = len(flowerbed)
        if n == 0:
            return True
        if k == 1:
            return flowerbed[0] == 0 and n == 1
        for i in range(0, k):
            if n == 0:
                break
            if i == 0 and (flowerbed[i] == 0 and flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            elif i == k-1 and (flowerbed[i] == 0 and flowerbed[i-1] == 0):
                flowerbed[i] = 1
                n -= 1
            if (i != 0 and i != k-1) and (flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                flowerbed[i] = i
                n -= 1

        return n == 0

print(Solution().canPlaceFlowers([1,0,0,0,1], 1))
print(Solution().canPlaceFlowers([1,0,0,0,1], 2))
print(Solution().canPlaceFlowers([1,0,1,0,1,0,1], 1))
print(Solution().canPlaceFlowers([0], 1))
