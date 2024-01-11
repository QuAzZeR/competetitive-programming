from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        answer = []
        for i in range(len(image)):
            answer.append(image[i][::-1])
            for j  in range(len(image[i])):
                if answer[i][j] == 1:
                    answer[i][j] = 0
                else:
                    answer[i][j] = 1
        return answer

print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(Solution().flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
