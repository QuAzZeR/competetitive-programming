from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(x, y):
            if y != 0:
                return gcd(y, x % y)
            else:
                return x

        n = len(nums)
        answer = 0
        for i in range(n):
            n1 = int(str(nums[i])[0])
            for j in range(i + 1, n):
                n2 = int(str(nums[j])[-1])
                if gcd(n1, n2) == 1:
                    answer += 1
        return answer


print(Solution().countBeautifulPairs([2, 5, 1, 4]))
print(Solution().countBeautifulPairs([11, 12, 21]))
