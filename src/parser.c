#include "../inc/parser.h"

parser* initParser(char* text) {
    parser* pr = (parser*)malloc(sizeof(parser));
    pr->st = initStack();
    pr->current = 0;
    pr->expression = (char*)malloc(sizeof(char) * (strlen(text)+1));
    pr->outSize = 1;
    pr->out = (char*)malloc(sizeof(char));
    *pr->out = NULL;
    strcpy(pr->expression, text);
    return pr;
}
void parse(parser* pr) {
    char temp[MAX_LENGTH] = {0};
    int tempLen = 0;
    while(pr->current < strlen(pr->expression)) {
        while(isIdentifier(pr->expression[pr->current])) temp[tempLen++] = pr->expression[pr->current++];
        if(tempLen) {
            pr->outSize += strlen(temp);
            pr->out = (char*)realloc(pr->out, pr->outSize);
            strncat(pr->out, temp, tempLen);
            tempLen = 0;
            temp[tempLen] = NULL;
        }

        while(isNumeric(pr->expression[pr->current])) temp[tempLen++] = pr->expression[pr->current++];
        if(tempLen) {
            pr->outSize += strlen(temp);
            pr->out = (char*)realloc(pr->out, pr->outSize);
            strncat(pr->out, temp, tempLen);
            tempLen = 0;
            temp[tempLen] = NULL;
        }




        if(pr->expression[pr->current] == ASCII_LEFT_PAREN)
            push(pr->st, STRING_LEFT_PAREN);
            
        else if (isOperand(pr->expression[pr->current])) {
            while(pr->st->sp > 0 && isStrongerOp(peek(pr->st)[0], pr->expression[pr->current])) {
                pr->out = (char*)realloc(pr->out,sizeof(char)*++pr->outSize);
                pr->out[pr->outSize-2] = pop(pr->st)[0];
                pr->out[pr->outSize-1] = '\0';
            }
            push(pr->st, asciiToString(pr->expression[pr->current]));
        }
        
        else if (pr->expression[pr->current] == ASCII_RIGHT_PAREN) {
            while(peek(pr->st)[0] != ASCII_LEFT_PAREN) {
                pr->out = (char*)realloc(pr->out,sizeof(char)*++pr->outSize);
                pr->out[pr->outSize-2] = pop(pr->st)[0];
                pr->out[pr->outSize-1] = '\0';
            }
            printf("%s\n",pop(pr->st));
        }

        
        pr->current++;
    }
    while(pr->st->sp > 0) {
        pr->out = (char*)realloc(pr->out,sizeof(char)*++pr->outSize);
        pr->out[pr->outSize-2] = pop(pr->st)[0];
        pr->out[pr->outSize-1] = '\0';
    }
}


bool isStrongerOp(char first, char second) {
    return (getOperandPriority(first) > getOperandPriority(second));
}


int getOperandPriority(char ch) {
    switch(ch) {
        case ASCII_PLUS:
        case ASCII_MINUS:
            return ADDITIVE_PRIORITY;
        case ASCII_MULTI:
        case ASCII_DIV:
            return MULTIPLICATIVE_PRIORITY;
        case ASCII_BANG:
        case ASCII_TILDA:
        case ASCII_CARRAT:
            return UNARY_PRIORITY;
        case ASCII_LEFT_PAREN:
        case ASCII_RIGHT_PAREN:
            return BLANK_PRIORITY;
    }
}

void freeParser(parser* par) {
    freeStack(par->st);
    free(par->expression);
    free(par->out);
    free(par);
    return;
}