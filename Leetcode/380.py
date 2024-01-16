import random
class RandomizedSet:

    def __init__(self):
        self.d = {}

    def insert(self, val: int) -> bool:
        result = val not in self.d
        self.d[val] = 1
        return result


    def remove(self, val: int) -> bool:
        result = val in self.d
        if result:
            del self.d[val]
        return result

    def getRandom(self) -> int:
        k = list(self.d.keys())
        idx = int(random.random() * len(k))
        return k[idx]

