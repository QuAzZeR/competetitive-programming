import heapq
from collections import defaultdict
from typing import List


import heapq


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        d = defaultdict(int)
        answer = []
        q = []
        l = len(nums)
        for i in range(l):
            n = nums[i]
            f = freq[i]
            d[n] += f
            heapq.heappush(q, (-d[n], n))
            while q:
                f, id = q[0]
                if d[id] == -f:
                    answer.append(-f)
                    break
                heapq.heappop(q)
        return answer


print(Solution().mostFrequentIDs([2, 3, 2, 1], [3, 2, -3, 1]))
print(Solution().mostFrequentIDs([5, 5, 3], [2, -2, 1]))
