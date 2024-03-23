class SmallestInfiniteSet:
    def __init__(self):
        self.d = {i: 1 for i in range(1, 10000)}

    def popSmallest(self) -> int:
        for i in range(1, 10000):
            if self.d[i]:
                self.d[i] = 0
                return i
        return 0

    def addBack(self, num: int) -> None:
        self.d[num] = 1


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
