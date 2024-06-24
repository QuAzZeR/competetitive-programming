from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flipped = 0
        answer = 0
        is_flipped = [0] * n
        for i in range(n):
            if i >= k:
                flipped ^= is_flipped[i - k]
            if flipped == nums[i]:
                if i + k > n:
                    return -1
                is_flipped[i] = 1
                flipped ^= 1
                answer += 1
        return answer


print(Solution().minKBitFlips([0, 1, 0], 1))
print(Solution().minKBitFlips([1, 1, 0], 2))
print(Solution().minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3))
