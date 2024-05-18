from typing import List


class Solution:
    def findComplement(self, num: int) -> int:
        answer = 0
        n = len(bin(num).split("b")[1])
        c = 2**n - 1

        return c ^ num


print(Solution().findComplement(5))
print(Solution().findComplement(1))
