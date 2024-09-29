from collections import defaultdict
class AllOne:

    def __init__(self):
        self.s = defaultdict(int)

    def inc(self, key: str) -> None:
        self.s[key] += 1


    def dec(self, key: str) -> None:
        self.s[key] -= 1
        if self.s[key] == 0:
            self.s.pop(key)


    def getMaxKey(self) -> str:
        if len(self.s) == 0:
            return ""
        v = max(self.s.values())
        for i in self.s:
            if self.s[i] == v:
                return i


    def getMinKey(self) -> str:
        if len(self.s) == 0:
            return ""
        v = min(self.s.values())
        for i in self.s:
            if self.s[i] == v:
                return i



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
