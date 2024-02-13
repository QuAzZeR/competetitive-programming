from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        l = len(nums)
        m = 2**l
        for i in range(m):
            s = f"{i:0{l}b}"
            c = []
            for i in range(l):
                if s[i] == "1":
                    c.append(nums[i])
            answer.append(c)
        return answer


print(Solution().subsets([1, 2, 3]))
print(Solution().subsets([0]))
