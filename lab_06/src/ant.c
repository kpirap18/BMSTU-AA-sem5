#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "ant.h"


void print_ants(sant ants[MAXCOUNTOFANT], int len)
{
    for (int i = 0; i < len; i++)
    {
        print_array(ants[i].way);
        print_array(ants[i].quere);
    }
    puts("\n");
}

void generate_ants_array(ant ants[MAXCOUNTOFANT], int len);

void ants_choose_way(ant ants[MAXCOUNTOFANT],
                     float matrix_p[N][N],
                     int matrix[N][N],
                     int len,
                     float alpha,
                     float beta);
