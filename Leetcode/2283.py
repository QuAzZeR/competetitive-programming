from typing import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        n = Counter(num)
        for i in range(len(num)):
            if n[str(i)] != int(num[i]):
                return False

        return True

print(Solution().digitCount('1210'))
print(Solution().digitCount('030'))
