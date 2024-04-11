class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]
        stack = "".join(stack).lstrip("0")
        if stack == "":
            return "0"
        return stack


print(Solution().removeKdigits("1432219", 3))
print(Solution().removeKdigits("10200", 1))
print(Solution().removeKdigits("10", 2))
print(Solution().removeKdigits("12", 1))
