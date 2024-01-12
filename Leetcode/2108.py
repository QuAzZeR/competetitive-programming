from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        answer = ''
        for i in words:
            if i == i[::-1]:
                answer = i
                break
        return answer
print(Solution().firstPalindrome(["abc","car","ada","racecar","cool"]))
print(Solution().firstPalindrome(["notapalindrome","racecar"]))
print(Solution().firstPalindrome(["def","ghi"]))
