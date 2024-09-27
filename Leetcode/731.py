from collections import defaultdict
class MyCalendarTwo:

    def __init__(self):
        self.calendar = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.calendar[start] += 1
        self.calendar[end] -= 1
        active_bookings = 0
        for i in sorted(self.calendar.keys()):
            active_bookings += self.calendar[i]
            if active_bookings >= 3:
                self.calendar[start] -= 1
                self.calendar[end] += 1
                if self.calendar[start] == 0:
                    del self.calendar[start]
                if self.calendar[end] == 0:
                    del self.calendar[end]

                return False
            if i > end:
                break

        return True


