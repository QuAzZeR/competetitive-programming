from typing import List
from collections import Counter

import json


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        def permu(expected, count, index, score, remain):
            if count == expected:
                self.answer = max(self.answer, score)
                return
            for i in range(index, n):
                current = words_letter_count[unexceed_words[i]]
                r = check_not_exceed(current["count"], remain)
                if len(r) != 0:
                    permu(expected, count + 1, i + 1, score + current["score"], r)

        def check_not_exceed(count, r):
            remain = {i: r[i] for i in r}
            for c in count:
                if count[c] > r[c]:
                    return {}
                else:
                    remain[c] = r[c] - count[c]
            return remain

        letters_count = Counter(letters)
        words_letter_count = dict()
        unexceed_words = []

        for word in words:
            words_letter_count[word] = {"count": Counter(word)}
            words_letter_count[word]["score"] = sum([score[ord(j) - 97] for j in word])

        for word in words:
            is_exceed = False
            for ch in word:
                if (
                    ch not in letters_count
                    or words_letter_count[word]["count"][ch] > letters_count[ch]
                ):
                    is_exceed = True
                    break
            if not is_exceed:
                unexceed_words.append(word)

        # print(json.dumps(words_letter_count, indent=4))
        # print(unexceed_words)
        n = len(unexceed_words)
        if n == 0:
            return 0
        self.answer = max(
            [words_letter_count[word]["score"] for word in unexceed_words]
        )

        for i in range(2, n + 1):
            print("EXPECTED", i)
            permu(i, 0, 0, 0, letters_count)

        return self.answer


print(
    Solution().maxScoreWords(
        ["dog", "cat", "dad", "good"],
        ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
        [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    )
)
print(
    Solution().maxScoreWords(
        ["xxxz", "ax", "bx", "cx"],
        ["z", "a", "b", "c", "x", "x", "x"],
        [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10],
    )
)
print(
    Solution().maxScoreWords(
        ["leetcode"],
        ["l", "e", "t", "c", "o", "d"],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    )
)
