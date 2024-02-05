from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        answer = sorted(d.items(), key=lambda x: -x[1])
        return "".join([key * value for key, value in answer])


print(Solution().frequencySort("tree"))
print(Solution().frequencySort("cccaaa"))
print(Solution().frequencySort("AabbB"))
