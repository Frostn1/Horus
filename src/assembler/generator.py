from src.assembler.stack import Stack
from src.utils.binary_tree import Node


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
def _do_arithmetic(arithmetic_op_str: str, value1: int, value2: int, stack: Stack) -> None:
    arithmetic_ops[arithmetic_op_str](value1, value2, stack)


def _do_stack(stack_op_str: str, value1: int, value2: int, stack: Stack) -> None:
    stack_ops[stack_op_str](value1, value2, stack)

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

def is_leaf(node: Node) -> bool:
    return node.left is None and node.right is None


def is_arithmetic(node: Node) -> bool:
    return node.data['raw'] in ['add',
                         'sub',
                         'div',
                         'mul']

def is_stack(node: Node) -> bool:
    return node.data['raw'] in ['push',
                                'pop']


def generate_code_for_tree(ast: Node, stack: Stack) -> None:
    if ast is None:
        return False, dict()
    if is_arithmetic(ast):

        # do_arithmetic(ast.data['raw'], left_value['value'], right_value['value'], stack)
    elif is_stack(ast):
        # left_value = ast.left.data if ast.left
        # _do_stack(ast.data['raw'], ast.left.data['value'], right_value['value'], stack )

def generate(ast_list: list[Node], stack: Stack) -> None:
    for ast in ast_list:
        traverse_tree(ast, stack)
