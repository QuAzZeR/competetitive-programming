class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        answer = ''
        m = min([str1, str2],key=lambda x: len(x))
        l1 = len(str1)
        l2 = len(str2)
        for i in range(len(m)):
            for j in range(len(m),-1, -1):
                divisor = m[i:j]
                lx = len(divisor)
                if lx == 0:
                    continue
                if divisor*(l1//lx) == str1 and divisor*(l2//lx) ==str2:
                    answer = max([answer, divisor], key=lambda z: len(z))
        return answer

print(Solution().gcdOfStrings("ABCABC", "ABC"))
print(Solution().gcdOfStrings("ABABAB", "ABAB"))
print(Solution().gcdOfStrings("LEET", "CODE"))
