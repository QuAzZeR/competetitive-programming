from typing import List
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = 0
        print(len(arr))
        if len(arr) == 2 or k > len(arr):
            return max(arr)
            
        c = 1
        while True:
            f = arr[0]
            s = arr[1]
            w,l = (f,s) if f > s else (s,f)
            
            if w == winner:
                c += 1
            else:
                winner = w
                c = 1
            if c == k:
                return w
            arr = [w]  + arr[2:] + [l]
            
print(Solution().getWinner([int(i) for i in input().split(',')], int(input())))
