from assembler.assembler import assemble


def main() -> None:
    code: list[str] = ["add 1, 1",
                             "sub 2, 1",
                             "mul 3, 1",
                             "div 4, 2",
                             "push 5",
                             "pop"]
    with open('../code/hello.aus') as file_p:
        code = file_p.readlines()
        assemble(code)


if __name__ == '__main__':
    main()
