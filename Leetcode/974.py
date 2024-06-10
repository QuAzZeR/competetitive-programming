from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        answer = 0
        s = 0
        m = {0: 1}
        for num in nums:
            s += num
            mod = s % k
            if mod < 0:
                mod += k
            if mod in m:
                answer += m[mod]
                m[mod] += 1
            else:
                m[mod] = 1
        return answer


print(Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
print(Solution().subarraysDivByK([5], 9))
