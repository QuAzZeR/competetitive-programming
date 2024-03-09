from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y, m, d = [int(i) for i in date1.split("-")]
        d1 = datetime(y, m, d)
        y, m, d = [int(i) for i in date2.split("-")]
        d2 = datetime(y, m, d)
        return abs((d2 - d1).days)


print(Solution().daysBetweenDates("2019-06-29", "2019-06-30"))
print(Solution().daysBetweenDates("2020-01-15", "2019-12-31"))
