class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        for i in range(len(self.s1) - 1):
            self.s2.append(self.s1.pop())
        element = self.s1.pop()

        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return element

    def peek(self) -> int:

        for i in range(len(self.s1) - 1):
            self.s2.append(self.s1.pop())
        element = self.s1[0]

        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return element

    def empty(self) -> bool:
        return self.s1 == []

