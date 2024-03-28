from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        answer = []
        pos = [i for i in nums if i > 0]
        neg = [i for i in nums if i < 0]
        n = len(nums) // 2
        for i in range(n):
            answer += [pos[i], neg[i]]
        return answer


print(Solution().rearrangeArray([3, 1, -2, -5, 2, -4]))
print(Solution().rearrangeArray([-1, 1]))
