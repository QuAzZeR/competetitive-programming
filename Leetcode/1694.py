class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")
        l = len(number)
        answer = []
        i = 0
        while i < l:
            if l - i == 4:
                answer.append(number[i : i + 2])
                answer.append(number[i + 2 : i + 4])
                i += 4
            elif l - i == 2:
                answer.append(number[i : i + 2])
                i += 2
            else:
                answer.append(number[i : i + 3])
                i += 3
        return "-".join(answer)


print(Solution().reformatNumber("1-23-45 6"))
print(Solution().reformatNumber("123 4-567"))
print(Solution().reformatNumber("123 4-5678"))
