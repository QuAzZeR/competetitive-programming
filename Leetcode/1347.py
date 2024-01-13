class Solution:
    def minSteps(self, s: str, t: str) -> int:
        first = {}
        second = {}
        for i in s:
            if i not in first :
                first[i] = 0
            first[i] +=1
        for i in t:
            if i not in second :
                second[i] = 0
            if i in first:
                if second[i] + 1 <= first[i]:
                    second[i] +=1
        answer = len(t) - sum([i for i in second.values()])
        return answer

print(Solution().minSteps("bab","aba"))
print(Solution().minSteps("leetcode","practice"))
print(Solution().minSteps("anagram","mangaar"))
