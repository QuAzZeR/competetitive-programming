from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f1 = defaultdict(int)
        f2 = defaultdict(int)
        for i in word1:
            f1[i] += 1
        for i in word2:
            f2[i] += 1
        f1_sort = sorted(f1.values())
        f2_sort = sorted(f2.values())

        return f1_sort == f2_sort and set(f1.keys()) == set(f2.keys())

print(Solution().closeStrings("abc", "bca"))
print(Solution().closeStrings("a", "aa"))
print(Solution().closeStrings("cabbba", "abbccc"))
