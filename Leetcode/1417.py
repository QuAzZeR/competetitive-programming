class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1:
            return s
        letter = [i for i in s if i >= "a" and i <= "z"]
        digit = [i for i in s if i >= "0" and i <= "9"]
        n = len(s)
        len_letter = len(letter)
        len_digit = len(digit)
        if len_letter == n or len_digit == n:
            return ""
        if abs(len_letter - len_digit) > 1:
            return ""
        answer = ""
        i_l = 0
        i_d = 0
        if len_letter > len_digit:
            answer += letter[i_l]
            i_l += 1
        if len_digit > len_letter:
            answer += digit[i_d]
            i_d += 1
        while i_l < len_letter and i_d < len_digit:
            if i_d > i_l:
                answer += letter[i_l] + digit[i_d]
            else:
                answer += digit[i_d] + letter[i_l]
            i_d += 1
            i_l += 1
        return answer


print(Solution().reformat("a0b1c2"))
print(Solution().reformat("leetcode"))
print(Solution().reformat("0123456789"))
print(Solution().reformat("covid2019"))
print(Solution().reformat("ab123"))
print(Solution().reformat("j"))
print(Solution().reformat("1"))
