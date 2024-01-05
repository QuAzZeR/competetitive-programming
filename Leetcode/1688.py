class Solution:
    def numberOfMatches(self, n: int) -> int:
        answer = 0
        while n != 1:
            if n%2 == 0:
                answer += int(n/2)
                n = int(n/2)
            else:
                answer += int((n-1)/2)
                n = int((n-1)/2)+1
            print(n, answer)
        return answer
print(Solution().numberOfMatches(7))
print(Solution().numberOfMatches(14))
