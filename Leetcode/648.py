from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=lambda x: len(x))
        sentences = sentence.split()
        n = len(sentences)
        for i in range(n):
            word = sentences[i]
            for d in dictionary:
                l = len(d)
                if word[:l] == d:
                    sentences[i] = d
                    break
        return " ".join(sentences)


print(
    Solution().replaceWords(
        ["cat", "bat", "rat"], "the cattle was rattled by the battery"
    )
)
print(Solution().replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"))
print(
    Solution().replaceWords(
        ["catt", "cat", "bat", "rat"], "the cattle was rattled by the battery"
    )
)
