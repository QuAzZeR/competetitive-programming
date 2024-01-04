from typing import List
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        answer = []
        n = {}
        for i in nums:
            if i not in n:
                n[i] = 0
            n[i] += 1
        while len(answer) != len(nums):
            a = min(n.keys())
            if n[a] > 1:
                n[a] -= 1
            else:
                del n[a]
            b = min(n.keys())
            if n[b] > 1:
                n[b] -= 1
            else:
                del n[b]
            answer.append(b)
            answer.append(a)
        return answer
print(Solution().numberGame([5,4,2,3]))
print(Solution().numberGame([2,5]))
print(Solution().numberGame([4,4,3,7]))
