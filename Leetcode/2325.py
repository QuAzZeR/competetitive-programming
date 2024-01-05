class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        current = 'a'
        m = {' ': ' '}
        for i in key:
            if current > 'z':
                break
            if i not in m:
                m[i] = current
                current = chr(ord(current) + 1)
        return ''.join([m[i] for i in message])

print(Solution().decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
print(Solution().decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))
