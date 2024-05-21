from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries) -> List[bool]:
        n = len(nums)
        j = 0
        map = [0]
        answer = []
        for i in range(1, n):
            if nums[i] % 2 == nums[i - 1] % 2:
                j += 1
            map.append(j)
        for q in queries:
            answer.append(map[q[0]] == map[q[1]])
        return answer


print(Solution().isArraySpecial([3, 4, 1, 2, 6], [[0, 4]]))
print(Solution().isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]))
