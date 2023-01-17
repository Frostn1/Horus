from src.assembler.error_handler import ErrorHandler
from src.assembler.generator import do_arithmetic, do_stack
from src.assembler.stack import Stack
from src.utils.binary_tree import Node
from src.assembler.validators import sem_validate_push_op, sem_validate_arith_op


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

def traverse_tree(ast: Node, stack: Stack) -> tuple[bool, dict]:
    if ast is None:
        return False, dict()
    if is_arithmetic(ast):
        is_valid, msg, error_column = sem_validate_arith_op(ast)
        ast.left.meta = ast.meta
        left_error, left_value = traverse_tree(ast.left, stack)
        if left_error:
            return True, dict()
        ast.right.meta = ast.meta
        right_error, right_value = traverse_tree(ast.right, stack)
        if right_error:
            return True, dict()
        if not is_valid:
            ErrorHandler.throw_error(
                'semantic',
                msg,
                ast.left.data['row_index'],
                error_column,
                ast.meta
            )
            return True, dict()
        # Hooray !
        # do_arithmetic(ast.data['raw'], left_value['value'], right_value['value'], stack)
    elif is_stack(ast):
        if ast.data['raw'] == 'push':
            is_valid, msg, error_column = sem_validate_push_op(ast)
            if not is_valid:
                ErrorHandler.throw_error(
                    'semantic',
                    msg,
                    ast.left.data['row_index'],
                    error_column,
                    ast.meta
                )
                return True, dict()
        left_error, left_value = traverse_tree(ast.left, stack)
        if left_error:
            return True, dict()
        right_error, right_value = traverse_tree(ast.right, stack)
        if right_error:
            return True, dict()


        # Hooray !
        # do_stack(ast.data['raw'], left_value['value'] if left_value else None, right_value['value'] if right_value else None, stack)

    elif is_leaf(ast):
        if ast.data['_type'] == 'reference':
            reference_value = stack.get_at(int(ast.data['_key']))
            if reference_value is None:
                ErrorHandler.throw_error(
                    'run time',
                    f'Referencing address must be lower than current stack top, got {ast.data["_key"]} expected *<{stack.length}',
                    ast.data['row_index'],
                    ast.data['column_index'] - 1,
                    ast.meta
                )
                return True, dict()
            return False, dict(value=reference_value)
        elif ast.data['_type'] == 'number':
            return False, dict(value=int(ast.data['raw']))


def visit_ast_list(ast_list: list[Node], stack: Stack):
    for ast in ast_list:
        traverse_tree(ast, stack)
