from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        for i in range(0, len(nums), 3):
            current = nums[i : i + 3]
            if (
                abs(current[1] - current[0]) > k
                or abs(current[2] - current[0]) > k
                or abs(current[2] - current[1]) > k
            ):
                return []
            answer.append(current)
        return answer


print(Solution().divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2))
print(Solution().divideArray([1, 3, 3, 2, 7, 3], 3))
print(Solution().divideArray([6, 10, 5, 12, 7, 11, 6, 6, 12, 12, 11, 7], 2))
