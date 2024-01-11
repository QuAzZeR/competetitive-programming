class Solution:
    def countPoints(self, rings: str) -> int:
        answer = 0
        rods = {i:set() for i in range(10)}
        for i in range(0, len(rings), 2):
            rods[int(rings[i+1])].add(rings[i])
        for i in rods:
            if len(rods[i]) == 3:
                answer += 1
        return answer
print(Solution().countPoints("B0B6G0R6R0R6G9"))
print(Solution().countPoints("B0R0G0R9R0B0G0"))
print(Solution().countPoints("G4"))
