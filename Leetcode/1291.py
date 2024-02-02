from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        answer = []
        min_l = min(len(str(low)), len(str(high)))
        max_l = max(len(str(low)), len(str(high)))
        for i in range(min_l, max_l + 1):
            for j in range(1, 9):
                current = ""
                is_exist = False
                for k in range(i):
                    if j + k > 9:
                        is_exist = True
                        break
                    current += str(j + k)

                if is_exist:
                    continue
                current = int(current)
                if current >= low and current <= high:
                    answer.append(current)
        return answer


print(Solution().sequentialDigits(100, 300))
print(Solution().sequentialDigits(1000, 13000))
print(Solution().sequentialDigits(10, 1000000000))
