from typing import List
from collections import Counter


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        d = Counter(nums)
        d = {i for i in d if d[i] == 2}
        x = 0
        for i in d:
            x ^= i
        return x


print(Solution().duplicateNumbersXOR([1, 2, 1, 3]))
print(Solution().duplicateNumbersXOR([1, 2, 3]))
print(Solution().duplicateNumbersXOR([1, 2, 2, 1]))
