from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        answer = 0
        for r in range(len(bank)):
            sum_r = sum([int(i) for i in bank[r]])
            is_break = False
            if sum_r == 0:
                continue
            for i in range(r+1, len(bank)):
                if is_break:
                    break
                sum_i = sum([int(i) for i in bank[i]])
                if sum_i == 0:
                    continue
                is_empty = True
                for j in range(r+1,i):
                    if sum([int(i) for i in bank[j]]):
                        is_empty = False
                        break
                if is_empty:
                    answer += sum_r * sum_i
                    is_break = True
        return answer 

print(Solution().numberOfBeams(["011001","000000","010100","001000"]))
print(Solution().numberOfBeams(["000","111","000"]))
