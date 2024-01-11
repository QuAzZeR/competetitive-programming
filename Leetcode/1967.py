from typing import List
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        answer = 0
        for i in patterns :
            if word.find(i) != -1:
                answer += 1
        return answer
print(Solution().numOfStrings(["a","abc","bc","d"], "abc"))
print(Solution().numOfStrings(["a","b","c"], "aaaaabbbbb"))
print(Solution().numOfStrings(["a","a","a"], "ab"))
