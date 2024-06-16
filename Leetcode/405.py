class Solution:
    def toHex(self, num: int) -> str:
        answer = ""
        if num == 0:
            return "0"
        if num < 0:
            num += 2**32
        m = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "a",
            11: "b",
            12: "c",
            13: "d",
            14: "e",
            15: "f",
        }
        minus = True if num < 0 else False
        num = abs(num)
        while num >= 1:
            answer += m[num % 16]
            num //= 16
        return ("-" if minus else "") + answer[::-1]


print(Solution().toHex(26))
print(Solution().toHex(-1))
