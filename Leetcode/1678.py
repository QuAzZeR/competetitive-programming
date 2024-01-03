class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace('()','o')
        command = command.replace('(al)','al')
        return command
print(Solution().interpret('G()(al)'))
print(Solution().interpret('G()()()()(al)'))
print(Solution().interpret('(al)G(al)()()G'))
