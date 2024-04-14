import re


class Solution:
    def findLatestTime(self, s: str) -> str:
        answer = ""
        s = s.replace("?", ".")
        print(s)
        for h in range(11, -1, -1):
            for m in range(59, -1, -1):
                x = "{:02d}:{:02d}".format(h, m)
                if len(re.findall(s, x)) != 0:
                    return x

        return answer


print(Solution().findLatestTime("1?:?4"))
print(Solution().findLatestTime("0?:5?"))
