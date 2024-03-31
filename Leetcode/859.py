from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            ds = Counter(s)
            for i in ds:
                if ds[i] > 1:
                    return True
            return False

        df = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                df.append(i)
            if len(df) > 2:
                return False
        return len(df) == 2 and s[df[0]] == goal[df[1]] and s[df[1]] == goal[df[0]]


print(Solution().buddyStrings("ab", "ba"))
print(Solution().buddyStrings("ab", "ab"))
print(Solution().buddyStrings("aa", "aa"))
print(Solution().buddyStrings("ab", "ca"))
