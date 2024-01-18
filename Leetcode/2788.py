from typing import List
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [i for i in f'{separator}'.join(words).split(separator) if i != '']
print(Solution().splitWordsBySeparator(words = ["one.two.three","four.five","six"], separator = "."))
print(Solution().splitWordsBySeparator(words = ["$easy$","$problem$"], separator = "$"))
print(Solution().splitWordsBySeparator(words = ["|||"], separator = "|"))
