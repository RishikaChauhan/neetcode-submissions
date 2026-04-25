class MinStack:

    def __init__(self):
        self.minstack = []

    def push(self, val: int) -> None:
        self.minstack.append(val)

    def pop(self) -> None:
        self.minstack.pop()

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.minstack[-1]

        while len(self.minstack):
            mini = min(mini, self.minstack[-1])
            tmp.append(self.minstack.pop())

        while len(tmp):
            self.minstack.append(tmp.pop())

        return mini
