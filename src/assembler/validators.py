from src.utils.binary_tree import Node


def syn_validate_arith_two_operands(token_list) -> tuple[bool, str, int]:
    if len(token_list) != 3:
        return False, f'Expected 3 operands, got {len(token_list)}', token_list[0]['column_index']

    return True, 'Success', 0


def syn_validate_push_op(token_list) -> tuple[bool, str, int]:
    if len(token_list) != 2:
        return False, f'Expected 2 operands, got {len(token_list)}', token_list[0]['column_index']
    return True, 'Success', 0


def syn_validate_pop_op(token_list) -> tuple[bool, str, int]:
    if len(token_list) != 1:
        return False, f'Expected 1 operands, got {len(token_list)}', token_list[0]['column_index']
    return True, 'Success', 0


def sem_validate_arith_op(ast: Node) -> tuple[bool, str, int]:
    valid_operand_types = ['number', 'reference']

    if ast.left.data['_type'] not in valid_operand_types:
        return False, f'First operand need to be one of the following [ {",".join(valid_operand_types)} ], got ( {ast.left.data["_type"]} )', \
            ast.left.data['column_index'] - len(ast.left.data['raw'])
    if ast.right.data['_type'] not in valid_operand_types:
        return False, f'Second operand need to be one of the following [ {",".join(valid_operand_types)} ], got ( {ast.right.data["_type"]} )', \
            ast.right.data['column_index'] - len(ast.right.data['raw'])
    return True, 'Success', 0


def sem_validate_push_op(ast: Node) -> tuple[bool, str, int]:
    valid_operand_types = ['number']
    if ast.left.data['_type'] not in valid_operand_types:
        return False, f'First operand need to be one of the following [ {",".join(valid_operand_types)} ], got ( {ast.left.data["_type"]} )', \
            ast.left.data['column_index'] - len(ast.left.data['raw'])
    return True, 'Success', 0
