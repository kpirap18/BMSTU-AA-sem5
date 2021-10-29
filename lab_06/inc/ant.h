#ifndef ANT_H
#define ANT_H

#include "define.h"
#include "array.h"

typedef struct
{
    sarray way;
    sarray quere;
} sant;

void print_ants(sant ants[MAXCOUNTOFANT], int len);

void generate_ants_array(ant ants[MAXCOUNTOFANT], int len);

void ants_choose_way(ant ants[MAXCOUNTOFANT],
                     float matrix_p[N][N],
                     int matrix[N][N],
                     int len,
                     float alpha,
                     float beta);


#endif // ANT_H
