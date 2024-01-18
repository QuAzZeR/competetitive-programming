class Solution:
    def repeatedCharacter(self, s: str) -> str:
        x = {}
        for i in s:
            if i in x:
                return i
            else:
                x[i] = 0
            x[i] += 1
        return ''
print(Solution().repeatedCharacter('abccbaacz'))
print(Solution().repeatedCharacter('abcdd'))
print(Solution().repeatedCharacter('abca'))
