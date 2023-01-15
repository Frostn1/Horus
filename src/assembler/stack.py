from src.utils.color_util import ColorUtil


class Stack:
    def __init__(self):
        self.stack: list[int] = []

    @property
    def length(self):
        return len(self.stack)

    @property
    def top(self):
        return self.stack[-1]

    def get_at(self, index: int):
        if index >= len(self.stack):
            return None

        return self.stack[(index * -1) - 1]

    def push(self, value: int):
        self.stack.append(value)

    def pop(self) -> int:
        value = self.stack.pop()
        return value

    def dump(self) -> None:
        ColorUtil.prPurple(
            '''
Stack dump:
-----------
        
        ''')
        for index, value in enumerate(self.stack):
            print(f'\t0x{index:04d}', end='\t')
            ColorUtil.prCyan(f'{value:06d}')
        print()
