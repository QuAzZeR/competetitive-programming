from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num = sum([1 for i in details if int(i[11:13])> 60])
        return num
print(Solution().countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))
print(Solution().countSeniors(["1313579440F2036","2921522980M5644"]))
