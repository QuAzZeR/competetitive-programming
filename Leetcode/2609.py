class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        m = 0
        for i in range(n):
            if s[i] == "1":
                continue
            l = 1
            zero = 1
            one = 0
            j = i + 1
            while j < n:
                if s[j] != "0":
                    break
                zero += 1
                j += 1
            while j < n:
                if s[j] != "1":
                    break
                one += 1
                j += 1
            if 0 not in [one, zero]:
                m = max(min(one, zero) * 2, m)

        return m


print(Solution().findTheLongestBalancedSubstring("01000111"))
print(Solution().findTheLongestBalancedSubstring("00111"))
print(Solution().findTheLongestBalancedSubstring("111"))
