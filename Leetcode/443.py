from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        answer = ''
        c = 1
        previous = None
        for i in range(len(chars)):
            if previous == None:
                answer += chars[i]
                previous = chars[i]
                continue
            if chars[i] != previous:
                if c != 1:
                    answer += str(c)
                answer += chars[i]
                previous = chars[i]
                c = 0
            c += 1
        if c != 1:
            answer += str(c)
        for i in range(len(answer)):
            chars[i] = answer[i]
        return len(answer)

print(Solution().compress(["a","a","b","b","c","c","c"]))
print(Solution().compress(["a"]))
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
