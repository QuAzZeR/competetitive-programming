from typing import List
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s_apple = sum(apple)
        capacity.sort(reverse=True)
        s_box = 0
        answer = 0
        for i in capacity:
            s_box += i
            answer += 1
            if s_box >= s_apple:
                break
        return answer

print(Solution().minimumBoxes([1,3,2], [4,3,1,5,2]))
print(Solution().minimumBoxes([5,5,5], [2,4,2,7]))