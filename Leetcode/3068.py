from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        temp = [[-1 for _ in range(2)] for _ in range(n)]

        def calculate(current, is_even):
            if current == n:
                return 0 if is_even else -float("inf")
            if temp[current][is_even] != -1:
                return temp[current][is_even]
            no_xor = nums[current] + calculate(current + 1, is_even)
            with_xor = (nums[current] ^ k) + calculate(current + 1, not is_even)

            m = max(no_xor, with_xor)
            temp[current][is_even] = m
            return m

        return calculate(0, 1)


print(Solution().maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]]))
print(Solution().maximumValueSum([2, 3], 7, [[0, 1]]))
print(
    Solution().maximumValueSum(
        [7, 7, 7, 7, 7, 7], 7, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
    )
)
