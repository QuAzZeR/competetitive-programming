from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        answer = []
        a = sorted([[i, arr[i]] for i in range(len(arr))], key=lambda x: (-x[1], x[0]))
        index = 0
        for i in range(len(arr) - 1):
            current = 0
            while True:
                if arr[i + 1] <= a[index][1] and a[index][0] > i:
                    current = a[index][1]
                    break
                index += 1
            answer.append(current)
        answer.append(-1)
        return answer


print(Solution().replaceElements([17, 18, 5, 4, 6, 1]))
print(Solution().replaceElements([400]))
