from typing import Counter


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        d = Counter(s)
        n = len(s)
        if letter in d:
            return int(d[letter]/n*100)
        return 0
print(Solution().percentageLetter("foobar","o"))
print(Solution().percentageLetter("jjjj","k"))
