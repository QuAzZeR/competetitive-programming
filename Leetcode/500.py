from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        answer = []
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        for word in words:
            s = set(word.lower())
            c1 = False
            c2 = False
            c3 = False
            for c in s:
                if c in r1:
                    c1 = True
                    break

            for c in s:
                if c in r2:
                    c2 = True
                    break
            for c in s:
                if c in r3:
                    c3 = True
                    break
            if c1 and not c2 and not c3:
                answer.append(word)
            if not c1 and c2 and not c3:
                answer.append(word)
            if not c1 and not c2 and c3:
                answer.append(word)
        return answer


print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))
print(Solution().findWords(["omk"]))
print(Solution().findWords(["adsdf", "sfd"]))
print(Solution().findWords(["Az"]))
