#ifndef ARRAY_H
#define ARRAY_H

#include "define.h"

typedef struct
{
    int len;
    int array[N];
} sarray;

void print_array(sarray cities);

void add_element(sarray *cities, const int element);

int get_element(sarray arr, int const index);

int del_element(sarray *cities, int element);

sarray copy_arr(sarray arr);

#endif // ARRAY_H
