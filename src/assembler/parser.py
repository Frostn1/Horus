from src.assembler.error_handler import ErrorHandler
from .validators import *
from src.utils.binary_tree import Node

valid_arithmetic_two_operands_operations = {
    'add': (syn_validate_arith_two_operands, 2),
    'sub': (syn_validate_arith_two_operands, 2),
    'div': (syn_validate_arith_two_operands, 2),
    'mul': (syn_validate_arith_two_operands, 2),
}

valid_stack_operations = {
    'push': (syn_validate_push_op, 1),
    'pop': (syn_validate_pop_op, 0)
}

valid_title_operations = {
    'title': (syn_validate_title_decl, 1),
    'run': (syn_validate_run_op, 1),
    'ret': (syn_validate_ret_op, 1),
    '!': (syn_validate_invoker_op, 0)
}

__all_operations__ = [
    valid_arithmetic_two_operands_operations,
    valid_stack_operations,
    valid_title_operations
]


def parse(token_list_list: list[list[dict]]) -> list[Node]:
    ast_list = []
    for token_list in token_list_list:
        for valid_operations_type in __all_operations__:
            if token_list[0]['_key'] in valid_operations_type:
                is_valid, msg, error_column = valid_operations_type[token_list[0]['_key']][0](token_list)
                if not is_valid:
                    ErrorHandler.throw_error(
                        'syntax',
                        msg,
                        token_list[0]['row_index'],
                        error_column,
                        ' '.join([token['raw'] for token in token_list])
                    )
                    continue
                semi_tree = Node(token_list[0])
                semi_tree.meta = ' '.join([token['raw'] for token in token_list])
                semi_tree.left = Node(token_list[1]) if valid_operations_type[token_list[0]['_key']][1] > 0 else None
                semi_tree.right = Node(token_list[2]) if valid_operations_type[token_list[0]['_key']][1] > 1 else None
                ast_list.append(semi_tree)

    return ast_list
