from typing import List
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for i in operations:
            if '+' in i:
                answer += 1
            elif '-' in i:
                answer -= 1

        return answer
        
print(Solution().finalValueAfterOperations(["--X","X++","X++"]))
print(Solution().finalValueAfterOperations(["++X","++X","X++"]))
print(Solution().finalValueAfterOperations(["X++","++X","--X","X--"]))
