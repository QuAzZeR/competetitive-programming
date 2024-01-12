from typing import List
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        answer = []
        c_min = 0
        c_max = len(s)
        for i in s:
            if i == 'I':
                answer.append(c_min)
                c_min += 1
            else:
                answer.append(c_max)
                c_max -=1
        answer.append(c_min)
        return answer

print(Solution().diStringMatch("IDID"))
print(Solution().diStringMatch("III"))
print(Solution().diStringMatch("DDI"))
