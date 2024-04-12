from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        n = len(height) - 1
        left_max = height[0]
        right_max = height[n]
        i = 0
        while i < n:
            if left_max <= right_max:
                answer += left_max - height[i]
                i += 1
                left_max = max(left_max, height[i])
            else:
                answer += right_max - height[n]
                n -= 1
                right_max = max(right_max, height[n])
        return answer


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([4, 2, 0, 3, 2, 5]))
