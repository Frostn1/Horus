#ifndef UTILS_H
#define UTILS_H

#include <io.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>

#define MAX_LENGTH 128

#define ASCII_CAPITAL_A 'A'
#define ASCII_CAPITAL_Z 'Z'
#define ASCII_SMALL_A 'a'
#define ASCII_SMALL_Z 'z'

#define ASCII_ZERO '0'
#define ASCII_NINE '9'
#define ASCII_SPACE ' '
#define ASCII_UNDERSCORE '_'

#define ASCII_PLUS '+'
#define ASCII_MINUS '-'
#define ASCII_DIV '/'
#define ASCII_MULTI '*'
#define ASCII_BANG '!'
#define ASCII_TILDA '~'
#define ASCII_CARRAT '^'
#define ASCII_LEFT_PAREN '('
#define ASCII_RIGHT_PAREN ')'

#define STRING_PLUS "+"
#define STRING_MINUS "-"
#define STRING_DIV "/"
#define STRING_MULTI "*"
#define STRING_BANG "!"
#define STRING_TILDA "~"
#define STRING_CARRAT "^"
#define STRING_LEFT_PAREN "("
#define STRING_RIGHT_PAREN ")"

char* readFile(char* filePath);

bool isIdentifier(char ch);
bool isOperand(char ch);

bool isNumeric(char ch);
bool isSpace(char ch);

char* asciiToString(char ch);





#endif // !UTILS_H