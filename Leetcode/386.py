from typing import List
import unittest


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1,n+1), key=lambda x: str(x))



class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.lexicalOrder(13), [1,10,11,12,13,2,3,4,5,6,7,8,9])
        self.assertEqual(s.lexicalOrder(2), [1,2])


if __name__ == "__main__":
    unittest.main()
