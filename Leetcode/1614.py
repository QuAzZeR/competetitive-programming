class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        answer = 0
        for i in s:
            if i == '(':
                count += 1
                if count > answer:
                    answer = count
            if i == ')':
                count -= 1
        return answer

print(Solution().maxDepth("(1+(2*3)+((8)/4))+1"))
print(Solution().maxDepth("(1)+((2))+(((3)))"))
