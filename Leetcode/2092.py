from typing import List


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        knows = [i for i in range(n)]
        knows[firstPerson] = 0
        meetings.sort(key=lambda x: x[2])
        i = 0
        l = len(meetings)
        while i < l:
            current_time = meetings[i][2]
            temp = []
            while i < l and meetings[i][2] == current_time:
                f, s, _ = meetings[i]
                ff = self.find_root(knows, f)
                ss = self.find_root(knows, s)
                knows[max(ff, ss)] = min(ff, ss)
                temp += [f, s]
                i += 1
            for j in temp:
                if self.find_root(knows, j) != 0:
                    knows[j] = j

        return [i for i in range(len(knows)) if self.find_root(knows, i) == 0]

    def find_root(self, groups, index):
        while groups[index] != index:
            index = groups[index]
        return index


print(Solution().findAllPeople(6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1))
print(Solution().findAllPeople(4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3))
print(Solution().findAllPeople(5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 1))
print(Solution().findAllPeople(11, [[5, 1, 4], [0, 4, 18]], 1))
