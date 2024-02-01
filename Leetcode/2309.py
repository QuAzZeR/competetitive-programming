class Solution:
    def greatestLetter(self, s: str) -> str:
        m = ""
        for i in range(65, 91):
            x = chr(i)
            if x in s and x.lower() in s:
                m = x
        return m


print(Solution().greatestLetter("lEeTcOdE"))
print(Solution().greatestLetter("arRAzFif"))
print(Solution().greatestLetter("AbCdEfGhIjK"))
