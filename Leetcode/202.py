class Solution:
    def isHappy(self, n: int) -> bool:
        answer = True
        d = {}
        while n != 1:
            s = str(n)
            new_value = sum(int(i) ** 2 for i in s)
            if new_value == 1:
                answer = True
                break
            n = new_value
            if n in d:
                answer = False
                break
            d[n] = 1
        return answer


print(Solution().isHappy(19))
print(Solution().isHappy(2))
