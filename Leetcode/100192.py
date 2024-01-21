from typing import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        c = sorted([(i, c[i]) for i in c], key=lambda x: (-x[1], x[0]))
        count = 1
        types = 0
        answer = 0
        for i,l in c:
            if count%8 == 1 :
                types += 1
            count +=1
            answer += types*l
        return answer


print(Solution().minimumPushes("abcde"))
print(Solution().minimumPushes("xyzxyzxyzxyz"))
print(Solution().minimumPushes("aabbccddeeffgghhiiiiii"))
