class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = None

    def push(self, val: int) -> None:
        if self.minValue == None:
            self.minValue = val
        else:
            self.minValue = min(self.minValue,val)
        self.stack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minValue = min(self.stack)
        else:
            self.minValue = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValue