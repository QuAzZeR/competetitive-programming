from typing import List
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        answer = 0
        for i in range(len(startTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                answer += 1
        return answer


print(Solution().busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4))
print(Solution().busyStudent(startTime = [4], endTime = [4], queryTime = 4))
