from typing import List
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        answer = [pref[0]]
        current = pref[0]
        for i in range(1,len(pref)):
            found = current ^ pref[i]
            current ^= found
            answer.append(found)

        return answer
print(Solution().findArray([5,2,0,3,1]))
print(Solution().findArray([13]))
