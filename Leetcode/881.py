from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        answer = 0
        people = sorted(people)
        i = 0
        j = len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            answer += 1

        return answer


print(Solution().numRescueBoats([1, 2], 3))
print(Solution().numRescueBoats([1, 2, 2, 3], 3))
print(Solution().numRescueBoats([3, 5, 3, 4], 5))
