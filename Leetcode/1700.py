from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = 0
        while len(students) != 0:
            if c == len(students):
                break
            std = students.pop(0)
            sw = sandwiches[0]
            if std != sw:
                students.append(std)
                c += 1
            else:
                sandwiches.pop(0)
                c = 0
        return len(students)


print(Solution().countStudents([1, 1, 0, 0], [0, 1, 0, 1]))
print(Solution().countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
