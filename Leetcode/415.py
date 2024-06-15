class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        long = max(num1, num2, key=lambda x: len(x))[::-1]
        short = min(num1, num2, key=lambda x: len(x))[::-1]
        nshort = len(short)
        nlong = len(long)
        if nshort == nlong:
            long = num1[::-1]
            short = num2[::-1]

        answer = ""
        add = 0
        for i in range(nshort):
            v = int(long[i]) + int(short[i]) + add
            add = v // 10
            answer += str(v % 10)
        if nshort != nlong:
            for i in range(nshort, nlong):
                v = int(long[i]) + add
                add = v // 10
                answer += str(v % 10)
        if add != 0:
            answer += str(add)
        return answer[::-1]


print(Solution().addStrings("11", "123"))
print(Solution().addStrings("456", "77"))
print(Solution().addStrings("0", "0"))
print(Solution().addStrings("0", "9"))
print(Solution().addStrings("1", "9"))
print(Solution().addStrings("9", "99"))
print(Solution().addStrings("123", "456"))
