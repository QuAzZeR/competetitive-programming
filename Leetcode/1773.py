from typing import List
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        answer = 0
        m = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        rule = m[ruleKey]
        for i in items:
            if i[rule].lower() == ruleValue.lower():
                answer += 1
        return answer

print(Solution().countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "Silver"))
print(Solution().countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],"type", "phone"))

