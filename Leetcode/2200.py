from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        answer = []
        match_index = [i for i in range(len(nums)) if nums[i] == key]
        for i in range(len(nums)):
            for j in match_index:
                if abs(i - j) <= k:
                    answer.append(i)
                    break
        return answer


print(Solution().findKDistantIndices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1))
print(Solution().findKDistantIndices([2, 2, 2, 2, 2], key=2, k=2))
