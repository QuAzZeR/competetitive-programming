from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        c = n//2
        for i in range(n):
            answer.append(c)
            c -= 1
        return answer

print(Solution().sumZero(5))
print(Solution().sumZero(3))
print(Solution().sumZero(1))

