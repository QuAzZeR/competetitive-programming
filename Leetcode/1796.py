class Solution:
    def secondHighest(self, s: str) -> int:
        d = set()
        for i in s:
            if i >= "0" and i <= "9":
                d.add(int(i))
        d = sorted(list(d))
        return d[1] if len(d) > 1 else -1


print(Solution().secondHighest("dfa12321afd"))
print(Solution().secondHighest("abc1111"))
