# TODO: Need to improve without using loop. I think condition should be enough to solve the problem
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        answer = 2
        rook = (a,b)
        bishop = (c,d)
        queen = (e,f)
        cp = list(bishop)
        x = 1
        y = 1
        if abs(queen[0]- bishop[0]) == abs(queen[1] - bishop[1]):
            if bishop[0] >  queen[0]:
                y =-1
            if bishop[1] > queen[1]:
                x = -1
            while True:
                if cp[0] < 1 or cp[0] > 8:
                    break
                if cp[1] < 1 or cp[1] > 8:
                    break
                cp[0] += y
                cp[1] += x
                if cp[0] == rook[0] and cp[1] == rook[1]:
                    break
                if cp[0] == queen[0] and cp[1] == queen[1]:
                    return 1
        x = 0
        y = 0
        cp = list(rook)
        if queen[0] == rook[0]:
            if queen[1] > rook[1]:
                x = 1
            else:
                x = -1
        if queen[1] == rook[1]:
            if queen[0] > rook[0]:
                y = 1
            else:
                y = -1
        if x == 0 and y == 0:
            return answer
        while True:
            if cp[0] < 1 or cp[0] > 8:
                break
            if cp[1] < 1 or cp[1] > 8:
                break

            cp[0] += y
            cp[1] += x
            if cp[0] == bishop[0] and cp[1] == bishop[1]:
                break
            if cp[0] == queen[0] and cp[1] == queen[1]:
                return 1
        return answer

print(2 == Solution().minMovesToCaptureTheQueen(a = 1, b = 1, c = 8, d = 8, e = 2, f = 3))
print(1 == Solution().minMovesToCaptureTheQueen(a = 5, b = 3, c = 3, d = 4, e = 5, f = 2))
print(2 == Solution().minMovesToCaptureTheQueen(a = 8, b = 2, c = 6, d = 2, e = 5, f = 2))
print(1 == Solution().minMovesToCaptureTheQueen(4,3,3,4,2,5))
print(2 == Solution().minMovesToCaptureTheQueen(1,8,4,3,2,7))
print(1 == Solution().minMovesToCaptureTheQueen(8,4,8,8,7,7))
print(1 == Solution().minMovesToCaptureTheQueen(8,5,2,4,5,7))
print(1 == Solution().minMovesToCaptureTheQueen(7,4,1,4,7,8))
print(1 == Solution().minMovesToCaptureTheQueen(5,8,8,8,1,8))
