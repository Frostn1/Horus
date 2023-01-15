from src.assembler.error_handler import ErrorHandler
from .validators import syn_validate_arith_two_operands, syn_validate_push_op, syn_validate_pop_op
from src.utils.binary_tree import Node

valid_arithmetic_two_operands_operations = [
    'add',
    'sub',
    'div',
    'mul',
]

valid_stack_operations = {
    'push': syn_validate_push_op,
    'pop': syn_validate_pop_op
}


def parse(token_list_list: list[list[dict]]) -> list[Node]:
    ast_list = []
    for token_list in token_list_list:
        if token_list[0]['raw'] in valid_arithmetic_two_operands_operations:
            is_valid, msg, error_column = syn_validate_arith_two_operands(token_list)
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
            semi_tree.left = Node(token_list[1])
            semi_tree.right = Node(token_list[2])
            ast_list.append(semi_tree)
        elif token_list[0]['raw'] in valid_stack_operations:
            is_valid, msg, error_column = valid_stack_operations[token_list[0]['raw']](token_list)
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
            semi_tree.left = Node(token_list[1]) if token_list[0]['raw'] == 'push' else None
            ast_list.append(semi_tree)
    return ast_list

