#include <stdio.h>

#include "matrix.h"
#include "colors.h"

void print_matrix(int matrix[N][N], int const len)
{
    printf("\t|");
    for (int i = 0; i < len; i++)
    {
        printf("%d\t", i);
    }
    printf("\n");
    for (int i = 0; i < len; i++)
    {
        printf("---------", i);
    }
    printf("\n");

    for (int i = 0; i < len; i++)
    {
        printf("%d\t|", i);
        for (int j = 0; j < len; j++)
        {
            printf(" &%d ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void fill_matrix(float matrix[N][N], int len, float fill)
{
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < i; j++)
        {
            matrix[i][j] = matrix[j][i] = fill;
        }
    }
}
