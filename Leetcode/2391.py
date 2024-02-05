from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m = 0
        p = 0
        g = 0
        tm = 0
        tp = 0
        tg = 0
        print("i", "m", "p", "g", "tm", "tp", "tg")
        for i in range(len(garbage)):
            if i >= 1:
                tm += travel[i - 1]
                tp += travel[i - 1]
                tg += travel[i - 1]
                print(">>>", tm, tp, tg)
                if "M" in garbage[i]:
                    m += tm
                    tm = 0
                if "G" in garbage[i]:
                    g += tg
                    tg = 0
                if "P" in garbage[i]:
                    p += tp
                    tp = 0

            m += garbage[i].count("M")
            p += garbage[i].count("P")
            g += garbage[i].count("G")
            print(i, m, p, g, tm, tp, tg)
        return m + p + g


print(Solution().garbageCollection(["G", "P", "GP", "GG"], travel=[2, 4, 3]))
print(Solution().garbageCollection(["MMM", "PGM", "GP"], travel=[3, 10]))
