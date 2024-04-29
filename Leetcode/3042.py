from typing import List
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(w1,w2):
            l1 = len(w1)
            l2 = len(w2)
            print(w1, w2[:l1], w2[l2-l1:])
            return w1 == w2[:l1] and w1 == w2[l2-l1:]
        answer = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                answer += isPrefixAndSuffix(words[i], words[j])
                print(answer)
        return answer


print(Solution().countPrefixSuffixPairs(["a","aba","ababa","aa"]))
print(Solution().countPrefixSuffixPairs(["pa","papa","ma","mama"]))
print(Solution().countPrefixSuffixPairs(["abab","ab"]))