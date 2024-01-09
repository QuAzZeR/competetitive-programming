class Solution:
    def finalString(self, s: str) -> str:
        answer = ''
        for i in s:
            if i == 'i':
                answer = answer[::-1]
            else:
                answer += i
        return answer
print(Solution().finalString("string"))
print(Solution().finalString("poiinter"))
