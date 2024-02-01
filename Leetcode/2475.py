from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        answer = 0
        if len(set(nums)) <= 2:
            return 0
        l = len(nums)
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        answer += 1
        return answer


print(Solution().unequalTriplets([4, 4, 2, 4, 3]))
print(Solution().unequalTriplets([1, 1, 1, 1, 1]))
