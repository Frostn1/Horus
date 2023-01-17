from src.utils.binary_tree import Node


def syn_validate_arith_two_operands(token_list) -> tuple[bool, str, int]:
    if len(token_list) != 3:
        return False, f'Expected 2 operands, got {len(token_list) - 1}', token_list[0]['column_index']
    if token_list[1]['_type'] == 'reference' and not token_list[1]['raw'][1:].isnumeric():
        return False, f'Reference must be followed by a number, got { token_list[1]["raw"][1:]}', token_list[1]['column_index'] + 1
    if token_list[2]['_type'] == 'reference' and not token_list[2]['raw'][1:].isnumeric():
        return False, f'Reference must be followed by a number, got { token_list[2]["raw"][1:]}', token_list[2]['column_index'] + 1

    return True, 'Success', 0


def syn_validate_push_op(token_list) -> tuple[bool, str, int]:
    if len(token_list) != 2:
        return False, f'Expected 1 operand, got {len(token_list) - 1}', token_list[0]['column_index']
    return True, 'Success', 0


def syn_validate_pop_op(token_list) -> tuple[bool, str, int]:
    if len(token_list) != 1:
        return False, f'Expected 0 operands, got {len(token_list) - 1}', token_list[0]['column_index']
    return True, 'Success', 0


def syn_validate_title_decl(token_list) -> tuple[bool, str, int]:
    if len(token_list) != 2:
        return False, f'Expected 1 operand, got {len(token_list) - 1}', token_list[0]['column_index']
    if not token_list[1]['raw'].isalpha():
        return False, f'Title identifier must be alpha, got {token_list[1]["raw"]}', token_list[1]['column_index'] - len(token_list[1]['raw'])
    return True, 'Success', 0


def syn_validate_run_op(token_list) -> tuple[bool, str, int]:
    if len(token_list) != 2:
        return False, f'Expected 1 operand, got {len(token_list) - 1}', token_list[0]['column_index']
    if not token_list[1]['raw'].isalpha():
        return False, f'First operand must be alpha, got {token_list[1]["raw"]}', token_list[1]['column_index'] - len(token_list[1]['raw'])
    return True, 'Success', 0


def syn_validate_invoker_op(token_list) -> tuple[bool, str, int]:
    if len(token_list) != 1:
        return False, f'Expected 0 operands, got {len(token_list) - 1}', token_list[0]['column_index']
    if not token_list[0]['raw'][1:].isalpha():
        return False, f'Invoker must be followed by a word literal, got {token_list[0]["raw"][1:]}', token_list[0]['column_index'] - len(token_list[0]['raw'])
    return True, 'Success', 0


def syn_validate_ret_op(token_list) -> tuple[bool, str, int]:
    if len(token_list) != 2:
        return False, f'Expected 1 operand, got {len(token_list) - 1}', token_list[0]['column_index']
    if token_list[1]['_type'] != 'reference':
        return False, f'First operand must be of type reference, got {token_list[1]["raw"]}', token_list[1]['column_index'] - len(token_list[1]['raw'])
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
