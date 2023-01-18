from src.assembler.error_handler import ErrorHandler
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

def _do_arithmetic(arithmetic_op_str: str, value1: int, value2: int, stack: Stack) -> None:
    arithmetic_ops[arithmetic_op_str](value1, value2, stack)


def _do_stack(stack_op_str: str, value1: int, value2: int, stack: Stack) -> None:
    stack_ops[stack_op_str](value1, value2, stack)



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


def _extract_value_int(ast: Node, stack: Stack) -> tuple[bool, int]:
    if ast is None:
        return False, -1
    if ast.data['_type'] == 'reference':
        reference_value = stack.get_at(int(ast.data['raw'][1:]))
        if reference_value is None:
            ErrorHandler.throw_error(
                'run time',
                f'Referencing address must be lower than current stack top, got {ast.data["_key"]} expected *<{stack.length}',
                ast.data['row_index'],
                ast.data['column_index'] - 1,
                ast.meta
            )
            return True, -1
        return False, reference_value
    elif ast.data['_type'] == 'number':
        return False, int(ast.data['raw'])
    ErrorHandler.throw_error(
        'run time',
        f'Unknown expression, got {ast.data["_type"]}',
        ast.data['row_index'],
        ast.data['column_index'] - 1,
        ast.meta
    )
    return True, -1


def generate_code_for_tree(ast: Node, stack: Stack) -> None:
    if ast is None:
        return False, dict()
    if is_arithmetic(ast):
        # lValueNode = None if ast.left is None else ast.left.data
        # rValueNode = None if ast.right is None else ast.right.data
        # print(f'[ sean .. arith ] ->\n- {ast.data}\n- {lValueNode}\n- {rValueNode}')
        l_error, l_value = _extract_value_int(
           ast.left,
           stack
        )
        r_error, r_value = _extract_value_int(
            ast.right,
            stack
        )
        if l_error or r_error:
            return
        _do_arithmetic(ast.data['raw'], l_value, r_value, stack)
    elif is_stack(ast):
        # l_value = None if ast.left is None else ast.left.data
        # r_value = None if ast.right is None else ast.right.data
        # print(f'[ sean .. stack ] ->\n- {ast.data}\n- {l_value}\n- {r_value}')
        l_error, l_value = _extract_value_int(
            ast.left,
            stack
        )
        r_error, r_value = _extract_value_int(
            ast.right,
            stack
        )
        if l_error or r_error:
            return
        _do_stack(ast.data['raw'], l_value, r_value, stack)
        pass
        # left_value = ast.left.data if ast.left
        # _do_stack(ast.data['raw'], ast.left.data['value'], right_value['value'], stack )


def generate(ast_list: list[Node], stack: Stack) -> None:
    for ast in ast_list:
        generate_code_for_tree(ast, stack)
