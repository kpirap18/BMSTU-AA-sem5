#include <stdio.h>
#include "antalgorithm.h"

void add_phenom(int matrix[N][N], float matrix_p[N][N], int len,
                int q, sant ants[MAXCOUNTOFANT])
{
    int fcity, scity;
    int cur_cost;
    float dtao = 0;

    for (int i = 0; i < len; i++)
    {
        cur_cost = get_cost(ants[i].way, matrix);
        dtao += (float)q / cur_cost;
    }

    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < ants[i].way.len - 1; j++)
        {
            fcity = ants[i].way.array[j];
            scity = ants[i].way.array[j + 1];

            matrix_p[fcity][scity] = matrix_p[fcity][scity] + dtao;
            matrix_p[scity][fcity] = matrix_p[scity][fcity] + dtao;
        }
    }
}

void delete_phenom(float matrix_p[N][N], int len, float p)
{
    float qq = 1 - p;

    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < i; j++)
        {
            matrix_p[i][j] = matrix_p[i][j] * qq;
            matrix_p[j][i] = matrix_p[j][i] * qq;
        }
    }
}

void phenom_correct(float matrix_p[N][N], int len)
{
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (matrix_p[i][j] <= 0.1)
            {
                matrix_p[i][j] = matrix_p[j][i] = 0.1;
            }
        }
    }
}

sarray ant_alg(int matrix[N][N], int len, sarray cities, int tmax,
               float p, float alpha, float beta)
{
    int q = calc_q(matrix, len);

    sarray best_way = copy_array(cities);
    add_element(&best_way, get_element(best_way, 0));

    int best_cost = get_cost(best_way, matrix);
    int cur_cost = 0;
    float matrix_p[N][N];
    fill_matrix(matrix_p, len, MINPHENOM);
    sant ants[MAXCOUNTOFANT];

//    printf("best_cost = %d\n", best_cost);


    // цикл по tmax
    for (int t = 0; t < tmax; t++)
    {
        generate_ants_array(ants, len);

        // по городам
        for (int i = 0; i < len - 1; i++)
        {
            ants_choose_way(ants, matrix_p, matrix, len, alpha, beta);
        }

        // добавить последний город
        for (int i = 0; i < len; i++)
        {
            add_element(&ants[i].way, get_element(ants[i].way, 0));
        }

        // поиск минимума
        for (int i = 0; i < len; i++)
        {
            cur_cost = get_cost(ants[i].way, matrix);
//            printf("best_cost = %d cur_cost = %d\n", best_cost, cur_cost);

            if (cur_cost < best_cost)
            {
                best_cost = cur_cost;
                best_way = copy_array(ants[i].way);
//                print_array(best_way, "best_way");
            }
        }

        delete_phenom(matrix_p, len, p);
        add_phenom(matrix, matrix_p, len, q, ants);
        phenom_correct(matrix_p, len);
    }

    return best_way;
}

int calc_q(int matrix[N][N], int len)
{
    int q = 0;

    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < len; j++)
        {
            q += matrix[i][j];
        }
    }
}


void print_matrix_pherom(float matrix_p[N][N], int len)
{
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < len; j++)
            printf("%f ", matrix_p[i][j]);
        printf("\n");
    }
}
