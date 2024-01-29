from datetime import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        map = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        return map[datetime(year, month, day).weekday()]

print(Solution().dayOfTheWeek(31,8,2019))
print(Solution().dayOfTheWeek(18,7,1999))
print(Solution().dayOfTheWeek(15,8,1993))
