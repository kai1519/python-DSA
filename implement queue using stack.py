class MyQueue:

    def __init__(self):
        self.item= []

    def push(self, x: int) -> None:
        self.item.insert(0,x)

    def pop(self) -> int:
        return self.item.pop()

    def peek(self) -> int:
        return self.item[-1]

    def empty(self) -> bool:
        return (len(self.item)==0)