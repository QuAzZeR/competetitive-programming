from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
print(Solution().getConcatenation([1,2,1]))
print(Solution().getConcatenation([1,3,2,1]))
