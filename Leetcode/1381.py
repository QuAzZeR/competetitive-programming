class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []


    def push(self, x: int) -> None:
        if len(self.stack) == self.max_size:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        print(k, val)
        s = min(len(self.stack), k)
        for i in range(s):
            self.stack[i] += val




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
