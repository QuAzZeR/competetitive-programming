from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 1
        r = position[-1] - position[0]
        answer = -1
        while l <= r:
            mid = l + (r - l) // 2
            last = position[0]
            b = 1
            for i in range(1, len(position)):
                if position[i] - last >= mid:
                    last = position[i]
                    b += 1
            if b >= m:
                answer = mid
                l = mid + 1
            else:
                r = mid - 1
        return answer


print(Solution().maxDistance([1, 2, 3, 4, 7], 3))
print(Solution().maxDistance([5, 4, 3, 2, 1, 1000000000], 2))
