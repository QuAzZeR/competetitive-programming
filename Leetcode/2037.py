from typing import List
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        answer = 0
        for i in range(len(seats)):
            answer += abs(seats[i] - students[i])
        return answer

print(Solution().minMovesToSeat([3,1,5], [2,7,4]))
print(Solution().minMovesToSeat([4,1,5,9], [1,3,2,6]))
print(Solution().minMovesToSeat([2,2,6,6], [1,3,2,6]))
