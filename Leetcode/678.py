class Solution:
    def checkValidString(self, s: str) -> bool:
        min_val = 0
        max_val = 0
        for i in s:
            if i == "(":
                min_val += 1
                max_val += 1
            elif i == ")":
                min_val -= 1
                max_val -= 1
            else:
                min_val -= 1
                max_val += 1
            if max_val < 0:
                return False
            if min_val < 0:
                min_val = 0
        return min_val == 0


print(Solution().checkValidString("()"))
print(Solution().checkValidString("(*)"))
print(Solution().checkValidString("(*))"))
