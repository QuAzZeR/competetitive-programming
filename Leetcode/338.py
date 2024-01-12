from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n+1)]

print(Solution().countBits(2))
print(Solution().countBits(5))
