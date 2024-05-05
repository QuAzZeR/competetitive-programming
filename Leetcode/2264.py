class Solution:
    def largestGoodInteger(self, num: str) -> str:
        answer = ""
        for i in range(0, 10):
            c = f"{i}{i}{i}"
            if f"{i}{i}{i}" in num:
                answer = c
        return answer


print(Solution().largestGoodInteger("6777133339"))
print(Solution().largestGoodInteger("2300019"))
print(Solution().largestGoodInteger("42352338"))
