from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        answer = []
        if turnedOn == 0:
            return ["0:00"]
        for i in range(1, 1024):
            b = "{:010b}".format(i)
            if b.count("1") == turnedOn:
                h = int(b[:4], 2)
                m = int(b[4:], 2)
                if h < 12 and m < 60:
                    answer.append(f"{h}:{m:02}")
        return answer


s = Solution()
print(s.readBinaryWatch(1))
print(s.readBinaryWatch(9))
