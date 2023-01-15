import time

from src.assembler.stack import Stack
from src.assembler.tokenizer import tokenize
from src.assembler.parser import parse
from src.assembler.visitor import visit_ast_list
from src.utils.binary_tree import Node


def assemble(input_code: list[str]) -> None:
    start_time: time.time = time.time()
    stack: Stack = Stack()
    token_list_list: list[list[dict]] = []
    for index, line in enumerate(input_code):
        token_list_for_line = tokenize(line, index + 1)
        token_list_list.append(token_list_for_line)
        print(token_list_for_line)
    stack.dump()
    ast_list: list[Node] = parse(token_list_list)
    visit_ast_list(ast_list, stack)
    stack.dump()
    print(f'[TOTAL TIME] --> {time.time() - start_time}s')
