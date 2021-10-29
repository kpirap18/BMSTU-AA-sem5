#include <stdio.h>
#include "bforce.h"


void get_routes(sarray *cities, sarray *res_,
                sarray result[MAXRECURSION],
                int matrix[N][N], int *len)
{
    int element;
    sarray tmp;

    if (cities->len != 0)
    {
        element = get_elem(*res_, 0);
        add_element(res_, element);
        result[*len] = *res_;
        (*len)++;

        del_element(res_, res_->len - 1);
    }
}

sarray get_shortest_path(sarray cities, int matrix[N][N])
{

}

int get_path_cost(sarray cities, int matrix[N][N])
{
    int cost = 0;

    for (int i = 0; i < cities.len - 1; i++)
    {
        cost += matrix[cities.array[i]][cities.array[i + 1]];
    }

    return cost;
}
