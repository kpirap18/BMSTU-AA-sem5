#include <stdio.h>

#include "city.h"



void print_cities(sarray cities, char name[LEN])
{
    for (int i = 0; i < cities.len; i++)
    {
        printf("%d: %c\t", cities.array[i], name[cities.array[i]]);
    }
    puts("\n");
}


int find_city(char cities[N], char city, int *len)
{
    int i = 0;

    while (i < len)
    {
        if (city == cities[i])
        {
            return i;
        }
        i++;
    }

    cities[i] = city;
    (*len)++;

    return i;
}


void create_cities_array(sarray *cities, int const len)
{
    cities->len = len;

    for (int = 0; i < len; i++)
    {
        cities->array[i] = i;
    }
}
