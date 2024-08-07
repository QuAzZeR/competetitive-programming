from typing import ByteString, List
import unittest


class Solution:
    def numberToWords(self, num: int) -> str:
        answer = ""
        digitString = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teenString = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tenString = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def helper(num):
            r = ""
            if num > 99:
                r += f'{digitString[num //100]} Hundred '
            num %= 100
            if num < 20 and num > 9:
                r += f'{teenString[num - 10]} '
            else:
                if num >= 20:
                    r += f'{tenString[num // 10]} '
                num %= 10
                if num > 0:
                    r += f'{digitString[num]} '
            return r
        if num == 0:
            return "Zero"
        s = ["Thousand", "Million", "Billion"]
        answer =  helper(num % 1000)
        num //= 1000
        for i in range(3):
            if num > 0 and num % 1000 > 0 :
                answer = helper(num%1000) + s[i] + " " + answer

            num //= 1000
        return answer.strip()



class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.numberToWords(123), "One Hundred Twenty Three")
        self.assertEqual(s.numberToWords(12345), "Twelve Thousand Three Hundred Forty Five")
        self.assertEqual(s.numberToWords(1234567), "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")


if __name__ == "__main__":
    unittest.main()
