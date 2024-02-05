from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        print(d.items(), ord("A"))
        answer = sorted(d.items(), key=lambda x: -x[1])
        print(answer)
        return "".join([key * value for key, value in answer])


print(Solution().frequencySort("tree"))
print(Solution().frequencySort("cccaaa"))
print(Solution().frequencySort("AabbB"))
