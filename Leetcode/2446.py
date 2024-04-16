from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        e1 = [int(i.replace(":", "")) for i in event1]
        e2 = [int(i.replace(":", "")) for i in event2]
        return (e1[0] >= e2[0] and e1[0] <= e2[1]) or (
            e2[0] >= e1[0] and e2[0] <= e1[1]
        )


print(Solution().haveConflict(["01:15", "02:00"], ["02:00", "03:00"]))
print(Solution().haveConflict(["01:00", "02:00"], ["01:20", "03:00"]))
print(Solution().haveConflict(["10:00", "11:00"], ["14:00", "15:00"]))
