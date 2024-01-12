class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0])-96
        y = int(coordinates[1])
        return (x%2 ==0 and y%2 != 0) or (x%2 !=0 and y%2 ==0)

print(Solution().squareIsWhite("a1"))
print(Solution().squareIsWhite("a2"))
print(Solution().squareIsWhite("h3"))
print(Solution().squareIsWhite("c7"))
