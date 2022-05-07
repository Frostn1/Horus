#include "../inc/utils.h"

char* readFile(char* filePath) {

    if (_access(filePath, 0) == -1) printf("file doesn't exist.\n"); 
    FILE* filePointer = fopen(filePath,"r");
    if (!filePointer) printf("can't open file\n");
    char* buffer = 0;
    long length;
    fseek(filePointer, 0, SEEK_END);
    length = ftell(filePointer);
    fseek(filePointer, 0, SEEK_SET);
    buffer = calloc(length, length);
    if (buffer) fread(buffer, 1, length, filePointer);
    fclose(filePointer);
    return buffer;
}


bool isIdentifier(char ch) {
    return ch >= ASCII_CAPITAL_A  && ch <= ASCII_CAPITAL_Z ||
        ch >= ASCII_SMALL_A && ch <= ASCII_SMALL_Z ||
        ch == ASCII_UNDERSCORE;
}

bool isOperand(char ch) {
    return ch == ASCII_BANG || ch == ASCII_CARRAT ||
        ch == ASCII_DIV || ch == ASCII_MINUS ||
        ch == ASCII_MULTI || ch == ASCII_TILDA ||
        ch == ASCII_PLUS || ch == ASCII_LEFT_PAREN ||
        ch == ASCII_RIGHT_PAREN;
}

bool isNumeric(char ch) {
    return ch >= ASCII_ZERO && ch <= ASCII_NINE;
}

bool isSpace(char ch) {
    return ch == ASCII_SPACE;
}

char* asciiToString(char ch) {
    switch(ch) {
        case ASCII_PLUS:
            return STRING_PLUS;
        case ASCII_MINUS:
            return STRING_MINUS;
        case ASCII_DIV:
            return STRING_DIV;
        case ASCII_MULTI:
            return STRING_MULTI;
        case ASCII_BANG:
            return STRING_BANG;
        case ASCII_TILDA:
            return STRING_TILDA;
        case ASCII_CARRAT:
            return STRING_CARRAT;
        case ASCII_LEFT_PAREN:
            return STRING_LEFT_PAREN;
        case ASCII_RIGHT_PAREN:
            return STRING_RIGHT_PAREN;
    }
}

