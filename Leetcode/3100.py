class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles
        drink = numBottles
        numBottles = 0
        while empty // numExchange > 0:
            drink += 1
            empty -= numExchange
            empty += 1
            numExchange += 1
            numBottles += 1
        return drink


print(Solution().maxBottlesDrunk(13, 6))
print(Solution().maxBottlesDrunk(10, 3))
