from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for i in range(left, right+1):
            s = str(i)
            is_self_deviding = True
            if len(s) == 1:
                answer.append(i)
                continue
            if '0' in s:
                continue
            for j in s:
                if i%int(j) != 0:
                    is_self_deviding = False
                    break
            if is_self_deviding:
                answer.append(i)
        return answer
print(Solution().selfDividingNumbers(1,22))
print(Solution().selfDividingNumbers(47, 85))
