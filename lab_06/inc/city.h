#ifndef CITY_H
#define CITY_H

#include "define.h"
#include "array.h"

int find_city(char cities[N], char city, int *len);

void print_cities(sarray cities, char name[LEN]);

void create_cities_array(sarray *cities, int const len);

#endif // CITY_H
