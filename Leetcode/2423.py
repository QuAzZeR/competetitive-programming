from collections import defaultdict
class Solution:
    def equalFrequency(self, word: str) -> bool:
        uniq_chr = defaultdict(int)
        for i in word:
            uniq_chr[i] += 1
        counts = sorted(uniq_chr.values())

        uniq_count = defaultdict(int)
        for i in counts:
            uniq_count[i] += 1
        k = sorted(list(uniq_count.keys()))
        if len(uniq_count) > 2:
            return False
        if len(uniq_count) == 1:
            return uniq_count[k[0]] == 1 or k[0] == 1

        mn,mx = sorted(k)
        if mn == 1:
            if uniq_count[mn] == 1:
                return True
            if mx == 2:
                return uniq_count[mn] == 1 or uniq_count[mx] == 1

        if mx - mn == 1:
            if uniq_count[mx] > uniq_count[mn]:
                return False
            if uniq_count[mn] == 1 or uniq_count[mx] == 1:
                return True
        return False
print(Solution().equalFrequency("abcc"))
print(Solution().equalFrequency("aazz"))
print(Solution().equalFrequency("abc"))
print(Solution().equalFrequency("cccaa"))
print(Solution().equalFrequency("ddaccb"))
print(Solution().equalFrequency("aca"))
print(Solution().equalFrequency("zz"))
print(Solution().equalFrequency("zzzzzzzzz"))
print(Solution().equalFrequency("caaaa"))
print(Solution().equalFrequency("ccccba"))
print(Solution().equalFrequency("abcdefghijklmnopqrstuvwxyznabcdefghijklmnopqrstuvwxyz"))
print(Solution().equalFrequency("aaaabbbbccc"))
