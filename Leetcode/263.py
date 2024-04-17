class Solution:
    def isUgly(self, n: int) -> bool:
        self.answer = False
        if n in [1, 2, 3, 5]:
            return True

        while n != 1:
            c = False
            if n % 2 == 0:
                n //= 2
                c = True
            if n % 3 == 0:
                n //= 3
                c = True
            if n % 5 == 0:
                n //= 5
                c = True
            if not c:
                return False
        return True


print(Solution().isUgly(6))
print(Solution().isUgly(1))
print(Solution().isUgly(14))
