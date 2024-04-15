import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.q = nums
        self.k = k
        heapq.heapify(self.q)

        while len(self.q) > self.k:
            heapq.heappop(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)

        while len(self.q) > self.k:
            heapq.heappop(self.q)
        return self.q[0]


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
