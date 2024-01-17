class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        answer =0
        for i in range(low, high +1):
            s = str(i)
            if len(s)%2 != 0:
                continue
            n = len(s)//2
            if sum(map(lambda x: int(x), s[:n])) == sum(map(lambda x: int(x), s[n:])):
                answer += 1

        return answer

print(Solution().countSymmetricIntegers(1,100))
print(Solution().countSymmetricIntegers(1200, 1230))
