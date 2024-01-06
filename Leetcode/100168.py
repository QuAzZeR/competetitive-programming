from typing import List
from itertools import permutations

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        m = max(nums+[k])
        l = len('{0:b}'.format(m))
        bit_nums = [format(i, f'0{l}b') for i in nums]
        xor = [0]*l
        for i in bit_nums:
            for j in range(l):
                if xor[j] == 1 :
                    if i[j] == '1':
                        xor[j] = 0
                    else:
                        xor[j] = 1
                elif xor[j] == 0 :
                    if i[j] == '1':
                        xor[j] = 1
                    else:
                        xor[j] = 0
        expectation = [int(i)  for i in format(k, f'0{l}b')]
        for i in range(l):
            if xor[i] != expectation[i]:
                answer +=1
        return answer



print(Solution().minOperations([2,1,3,4], 1))
print(Solution().minOperations([2,0,2,0], 0))
print(Solution().minOperations([3,5,1,1], 19))
