class Solution:
    def splitNum(self, num: int) -> int:
        n1 = ""
        n2 = ""
        s = sorted(str(num))
        l = len(s)
        for i in range(l):
            if i % 2 == 0:
                n1 += s[i]
            else:
                n2 += s[i]
        return int(n1) + int(n2)


print(Solution().splitNum(4325))
print(Solution().splitNum(687))
