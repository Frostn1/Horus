#ifndef PARSER_H
#define PARSER_H

#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#include "stack.h"
#include "utils.h"

#define ADDITIVE_PRIORITY 0x0B // + -
#define MULTIPLICATIVE_PRIORITY 0x0C // * / %
#define UNARY_PRIORITY 0x0D // ! ~ ^
#define BLANK_PRIORITY 0x00


typedef struct parser {
    stack* st;
    char* expression;
    char* out;
    int current;
    int outSize;
} parser;

parser* initParser(char* text);
void freeParser(parser* par);
void parse(parser* pr);

bool isStrongerOp(char first, char second);
int getOperandPriority(char ch);
#endif // !PARSER_H