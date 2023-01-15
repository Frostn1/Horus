from src.assembler.error_handler import ErrorHandler

valid_tokens = [
    'add',
    'sub',
    'div',
    'mul',
    'push',
    'pop'
]


def is_space(char: chr):
    return char == ' ' or char == '\t' or char == '\n'


def validate_token(token_str: str) -> tuple[bool, str, dict]:
    if token_str in valid_tokens:
        return False, '', {'raw': token_str.lower(), '_key': valid_tokens.index(token_str), '_type': 'expression'}
    elif token_str.isnumeric():
        return False, '', {'raw': token_str, '_key': '', '_type': 'number'}
    elif token_str[0] == '@':
        if token_str[1:].isnumeric():
            return False, '', {'raw': token_str, '_key': token_str[1:], '_type': 'reference'}
        return True, 'Reference must be followed by a number', dict()
    return False, '', {'raw': token_str, '_key': '', '_type': 'undefined'}

def tokenize(input_str: str, row_index: int) -> list[dict]:
    token_list = []
    current_token = ''
    column_index = 1
    for char in input_str:
        if is_space(char) and current_token:
            error, msg, validated_token = validate_token(current_token)
            if error:
                ErrorHandler.throw_error(
                    'syntax',
                    msg,
                    row_index,
                    column_index - len(current_token),
                    input_str
                )

            else:
                token_list.append(validated_token | dict(row_index=row_index, column_index=column_index))
            current_token = ''

        elif is_space(char):
            column_index += 1
            continue
        else:
            current_token += char
        column_index += 1
    if current_token:
        error, msg, validated_token = validate_token(current_token)
        if error:
            ErrorHandler.throw_error(
                'syntax',
                msg,
                row_index,
                column_index - len(current_token),
                input_str
            )

        else:
            token_list.append(validated_token | dict(row_index=row_index, column_index=column_index))
    return token_list
