class RecentCounter:

    def __init__(self):
        self.history = []

    def ping(self, t: int) -> int:
        self.history.append(t)
        return len([i for i in self.history if i >= t-3000 and i <= t])
