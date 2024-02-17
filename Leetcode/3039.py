from collections import defaultdict


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        answer = ""
        d = {}
        for i in range(len(s)):
            c = s[i]
            if c not in d:
                d[c] = []
            d[c].append(i)
        for i in d:
            x = d[i]
            d[i] = sorted(x, reverse=True)

        answer = [""] * len(s)
        while True:
            l = [len(d[i]) for i in d]
            mx = max(l)
            mi = min(l)
            if mi == 1 and mx == 1:
                break
            if mi == 0 and mx == 1:
                break
            d = {i: d[i] for i in d if len(d[i]) != 0}
            for i in d:
                d[i].pop()
        for i in d:
            for j in d[i]:
                answer[j] = i
        return "".join([i for i in answer if i != ""])


print(Solution().lastNonEmptyString("aabcbbca"))
print(Solution().lastNonEmptyString("aabcbbcaab"))
print(Solution().lastNonEmptyString("abcd"))
print(Solution().lastNonEmptyString("abcddcba"))
