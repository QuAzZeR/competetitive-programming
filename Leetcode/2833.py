from collections import Counter


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        s = set(moves)
        if len(s) == 1 or (len(s) == 2 and "_" in set(moves)):
            return len(moves)
        d = Counter(moves)
        r = d["R"]
        l = d["L"]
        _ = d["_"]
        if r > l:
            return r - l + _
        elif r <= l:
            return l - r + _
        return 0


print(Solution().furthestDistanceFromOrigin("_______"))
print(Solution().furthestDistanceFromOrigin("R______"))
print(Solution().furthestDistanceFromOrigin("L______"))
print(Solution().furthestDistanceFromOrigin("L_RL__R"))
print(Solution().furthestDistanceFromOrigin("_R__LL_"))
