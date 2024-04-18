from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        n = len(arr)
        first_five = int(n * 0.05)
        end_five = n - first_five
        left = arr[first_five:end_five]
        return sum(left) / len(left)


print(Solution().trimMean([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]))
print(
    Solution().trimMean([6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0])
)
print(
    Solution().trimMean(
        [
            6,
            0,
            7,
            0,
            7,
            5,
            7,
            8,
            3,
            4,
            0,
            7,
            8,
            1,
            6,
            8,
            1,
            1,
            2,
            4,
            8,
            1,
            9,
            5,
            4,
            3,
            8,
            5,
            10,
            8,
            6,
            6,
            1,
            0,
            6,
            10,
            8,
            2,
            3,
            4,
        ]
    )
)
