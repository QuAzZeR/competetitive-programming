from typing import List
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(sentence.split(' ')) for sentence in sentences])
print(Solution().mostWordsFound(["alice and bob love leetcode","i think so too","this is great thanks very much"]))
print(Solution().mostWordsFound(["please wait","continue to fight","continue to win"]))
