from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in operations:
            if i == 'C':
                score = score[:-1]
            elif i == '+':
                score.append(score[-1] + score[-2])
            elif i == 'D':
                score.append(score[-1]*2)
            else:
                score.append(int(i))

        return sum(score)

print(Solution().calPoints(["5","2","C","D","+"]))
print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))
print(Solution().calPoints(["1","C"]))
