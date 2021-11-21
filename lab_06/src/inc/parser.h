#ifndef PARSER_H
#define PARSER_H

#include <stdio.h>

#include "array.h"
#include "define.h"

int parser(FILE *f, char cities[N], int matrix[N][N]);

int parser_to_dot(char fname[20], char cities[N], int matrix[N][N], 
                  sarray result, int len, char color[10]);

#endif // PARSER_H
