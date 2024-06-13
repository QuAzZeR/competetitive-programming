from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        new_words = [words[0]]

        for i in range(1, len(words)):
            if not sorted(words[i]) == sorted(words[i - 1]):
                new_words.append(words[i])
        return new_words


print(Solution().removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"]))
print(Solution().removeAnagrams(["a", "b", "c", "d", "e"]))
