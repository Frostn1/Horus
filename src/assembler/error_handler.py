from src.utils.color_util import ColorUtil


class ErrorHandler:
    @staticmethod
    def throw_error(error_type: str, error_message: str, row_index: int, column_index: int, row_raw: str):
        '''
        [ syntax error ] -> expected bla bla bla
        |
        |   add 1 'hello'
        | --------^
        row 1 <> column 12


        :param error_type:
        :param error_message:
        :param row_index:
        :param column_index:
        :param row_raw:
        :return:
        '''

        ColorUtil.prYellow('[ ', end='')
        print(f'{error_type} error', end='')
        ColorUtil.prYellow(' ]', end='')
        print(f' => ', end='')
        ColorUtil.prRed(error_message)
        print(f'|')
        print(f'|', end='\t')
        ColorUtil.prLightPurple(row_raw.strip())
        print(f'|', end=' ')
        ColorUtil.prCyan(f'{"-" * (column_index - 3)}^')
        print(f'row {row_index} <> column {column_index}\n')
