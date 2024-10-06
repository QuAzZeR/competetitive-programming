from typing import List
import unittest


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        w1 = sentence1.split()
        w2 = sentence2.split()
        n1 = len(w1)
        n2 = len(w2)
        if n1 < n2:
            w1, w2 = w2, w1
            n1, n2 = n2, n1
        s = 0
        e = 0
        while s < n2 and w1[s] == w2[s]:
            s += 1
        while e < n2 and w1[n1 - e -1] == w2[n2 - e -1]:
            e += 1


        return s +e >= n2


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.areSentencesSimilar("My name is Haley", "My Haley"), True)
        self.assertEqual(s.areSentencesSimilar("of", "A lot of words"), False)
        self.assertEqual(s.areSentencesSimilar("Eating right now", "Eating"), True)


if __name__ == "__main__":
    unittest.main()
