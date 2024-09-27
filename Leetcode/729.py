class MyCalendar:

    def __init__(self):
        self.calendar =[]

    def book(self, start: int, end: int) -> bool:
        if len(self.calendar) == 0:
            self.calendar.append((start,end))
            return True
        for i in self.calendar:
            if not (end <= i[0] or start >= i[1]):
                return False
        self.calendar.append((start,end))
        return True
