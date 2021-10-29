#include <stdio.h>

#include "matrix.h"
#include "colors.h"

void print_matrix(int matrix[N][N], int const len)
{
    for (int i = 0; i < len; i++)
    {
        printf("%d\t", i);
    }
    puts("");

    for (int i = 0; i < len; i++)
    {
        printf("%d ", i);
        for (int j = 0, j < len, j++)
        {
            printf("%d\t", matrix[i][j]);
        }
        puts("");
    }
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
