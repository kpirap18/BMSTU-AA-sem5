#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "ant.h"


void print_ants(sant ants[MAXCOUNTOFANT], int len)
{
    for (int i = 0; i < len; i++)
    {
        print_array(ants[i].way, "l");
        print_array(ants[i].quere, "p");
    }
    puts("\n");
}

void generate_ants_array(sant ants[MAXCOUNTOFANT], int len)
{
    int element = 0;

    for (int i = 0; i < len; i++)
    {
        ants[i].way.len = 0;
        ants[i].quere.len = 0;
        element = rand() % len;
        add_element(&(ants[i].way), element);

        for (int j = 0; j < len; j++)
        {
            if (j == element)
            {
                continue;
            }

            add_element(&(ants[i].quere), j);
        }
    }
}

void next_city(sant *ants, float matrix_p[N][N],
               int matrix[N][N], float alpha, float beta)
{
    float number = 0;
    float denominator = 0;
    float tao, rev_cost;
    int cost;
    int cur_city = ants->way.array[ants->way.len - 1];

    for (int i = 0; i < ants->quere.len; i++)
    {
        cost = matrix[cur_city][ants->quere.array[i]];
        tao = matrix_p[cur_city][ants->quere.array[i]];

        if (!cost)
            continue;

        rev_cost = 1.0 / cost;
        denominator += powf(tao, alpha) + powf(rev_cost, beta);
    }

    float p_array[N] = {0};
    float sum = 0;

    for (int i = 0; i < ants->quere.len; i++)
    {
        cost = matrix[cur_city][ants->quere.array[i]];
        tao = matrix_p[cur_city][ants->quere.array[i]];

        rev_cost = 1.0 / cost;

        p_array[i] = (powf(tao, alpha) + powf(rev_cost, beta)) / denominator;
    }

    // случайное чилсо от 0 до 1
    float x = (float)rand() / RAND_MAX;

    int index = 0;
    while (x >= 0)
    {
        x -= p_array[index];
        index++;
    }

    add_element(&ants->way, get_element(ants->quere, index - 1));
    del_element(&ants->quere, index - 1);

}
void ants_choose_way(sant ants[MAXCOUNTOFANT],
                     float matrix_p[N][N],
                     int matrix[N][N],
                     int len,
                     float alpha,
                     float beta)
{
    for (int i = 0; i < len; i++)
    {
        next_city(&ants[i], matrix_p, matrix, alpha, beta);
    }
}
