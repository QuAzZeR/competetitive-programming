class Solution:
    def freqAlphabets(self, s: str) -> str:
        def convert(n):
            return chr(97 +n -1)
        answer = ''
        i = 0
        while i < len(s):
            if i +2 < len(s) and s[i+2] == '#':
                if s[i+2] == '#':
                    answer += convert(int(''.join(s[i:i+2])))
                    i+=2
            else:
                answer += convert(int(s[i]))
            i+=1
        return answer
print(Solution().freqAlphabets("10#11#12"))
print(Solution().freqAlphabets("1326#"))
