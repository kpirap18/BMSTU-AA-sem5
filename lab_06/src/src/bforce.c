#include <stdio.h>
#include "bforce.h"

int get_cost(sarray cities, int matrix[N][N])
{
    int cost = 0;

    for (int i = 0; i < cities.len - 1; i++)
        cost += matrix[cities.array[i]][cities.array[i + 1]];

    return cost;
}

void get_routes(sarray *cities, sarray *res_,
                sarray result[MAXRECURSION], int *len)
{
    int element;
    sarray buf;

    if (!cities->len)
    {
        add_element(res_, get_element(*res_, 0));
        
        result[*len] = *res_;
        (*len)++;

        del_element(res_, res_->len - 1);

//        print_array(*cities, "cities");
//        print_array(*res_, "res_arr");
//        printf("count = %d\n\n", *len);
    }

    for (int i = 0; i < cities->len; i++)
    {
        element = get_element(*cities, i);

        add_element(res_, element);

        buf = copy_array(*cities);
        del_element(&buf, i);

        get_routes(&buf, res_, result, len);

        del_element(res_, res_->len - 1);
    }
}

sarray get_shortest_path(sarray *cities, int matrix[N][N])
{
    sarray result[MAXRECURSION];
    sarray res_;

    int min_index = 0;
    int min_cost;
    int cur_cost;

    int len_routes = 0;

    // начало
    del_element(cities, 0);
    add_element(&res_, 0);

    // запуск поиска пути
    get_routes(cities, &res_, result, &len_routes);

    min_cost = get_cost(result[min_index], matrix);

    for (int i = 1; i < len_routes; i++)
    {
        cur_cost = get_cost(result[i], matrix);
        if (cur_cost < min_cost)
        {
            min_cost = cur_cost;
            min_index = i;
        }
    }
    return result[min_index];
}

