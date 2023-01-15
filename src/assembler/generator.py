from src.assembler.stack import Stack


def _do_add(value1: int, value2: int, stack: Stack) -> None:
    _out = value1 + value2
    stack.push(_out)


def _do_sub(value1: int, value2: int, stack: Stack) -> None:
    _out = value1 - value2
    stack.push(_out)


def _do_mul(value1: int, value2: int, stack: Stack) -> None:
    _out = value1 * value2
    stack.push(_out)


def _do_div(value1: int, value2: int, stack: Stack) -> None:
    _out = value1 // value2
    stack.push(_out)


def _do_push(value1: int, value2: None, stack: Stack) -> None:
    stack.push(value1)


def _do_pop(value1: None, value2: None, stack: Stack) -> None:
    stack.pop()


arithmetic_ops = {
    'add': _do_add,
    'sub': _do_sub,
    'mul': _do_mul,
    'div': _do_div
}

stack_ops = {
    'push': _do_push,
    'pop': _do_pop
}


def do_arithmetic(arithmetic_op_str: str, value1: int, value2: int, stack: Stack) -> None:
    arithmetic_ops[arithmetic_op_str](value1, value2, stack)


def do_stack(stack_op_str: str, value1: int, value2: int, stack: Stack) -> None:
    stack_ops[stack_op_str](value1, value2, stack)