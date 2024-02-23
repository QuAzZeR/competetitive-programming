from typing import List
from queue import Queue


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        m = {}
        for s, d, p in flights:
            if s not in m:
                m[s] = {}
            if d not in m[s]:
                m[s][d] = p
        if src not in m:
            return -1
        cheapest_price = [float("inf")] * n
        q = Queue()
        q.put((src, 0))
        stops = 0
        while not q.empty() and stops <= k:
            queue_size = q.qsize()
            for i in range(queue_size):
                current, current_price = q.get()
                if current not in m:
                    continue
                for next in m[current]:
                    price = m[current][next]
                    if current_price + price >= cheapest_price[next]:
                        continue
                    cheapest_price[next] = price + current_price
                    q.put((next, cheapest_price[next]))
            stops += 1
        return cheapest_price[dst] if cheapest_price[dst] != float("inf") else -1


print(
    Solution().findCheapestPrice(
        4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1
    )
)
print(Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
print(Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
print(
    Solution().findCheapestPrice(
        5, [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]], 2, 1, 1
    )
)

print(
    Solution().findCheapestPrice(
        5,
        [[3, 0, 8], [1, 4, 1], [1, 0, 4], [1, 3, 3], [3, 4, 1], [2, 3, 3], [2, 0, 10]],
        1,
        4,
        4,
    )
)
