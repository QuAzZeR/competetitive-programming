from typing import List
import unittest


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        answer = []
        m = {str(i): str(mapping[i])
            for i in range(len(mapping))
        }
        for i in nums:
            answer.append((int(''.join([m[j] for j  in str(i)])),i))
        print(answer)
        answer.sort(key=lambda x: x[0])
        return [i[1] for i in answer]


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.sortJumbled( mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]), [338,38,991])
        self.assertEqual(s.sortJumbled(mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123]),  [123,456,789])


if __name__ == "__main__":
    unittest.main()
