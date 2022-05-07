#include <stdio.h>
#include <stdlib.h>
#include <io.h>

#include "../inc/stack.h"
#include "../inc/parser.h"
#include "../inc/utils.h"

int main(int argc, char** argv) {
    // char* code = "2 + 1";
    // parser* par = initParser(code);
    // parse(par);
    // printf("%s\n%s\n", code, par->out);
    parser* par = NULL;
    char buffer[MAX_LENGTH] = {0};
        for(;;) {
            printf("~ ");
            fgets(buffer, MAX_LENGTH, stdin);
            buffer[strlen(buffer)-1] = '\0';
            if(!strcmp(buffer,"")) break;
            par = initParser(buffer);
            parse(par);
            printf("%s\n", par->out);
        }
    freeParser(par);


    return 0;
}