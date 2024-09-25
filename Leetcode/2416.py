from typing import List
import unittest


class Trie:
    def __init__(self):
        self.score = 0
        self.children = {}
    def add(self, s, i):
        if i:
            self.score += 1
        if i == len(s):
            return
        if not self.children.get(s[i]):
            self.children[s[i]] = Trie()
        self.children[s[i]].add(s, i+1)
    def dfs(self, s, i):
        if i == len(s):
            return self.score
        return self.score + self.children[s[i]].dfs(s, i+1)

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add(word, 0)
        answer = []
        for word in words:
            answer.append(trie.dfs(word, 0))
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.sumPrefixScores(["abc","ab","bc","b"]), [5,4,3,2])
        self.assertEqual(s.sumPrefixScores(["abcd"]), [4])


if __name__ == "__main__":
    unittest.main()
