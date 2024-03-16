from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            l = len(str(num))
            m = max([int(i) for i in str(num)])
            answer += int(str(m) * l)

        return answer


print(Solution().sumOfEncryptedInt([1, 2, 3]))
print(Solution().sumOfEncryptedInt([10, 21, 31]))
