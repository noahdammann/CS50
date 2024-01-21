#include <cs50.h>
#include <stdio.h>

float discount(float price, percent_off);

int main(void)
{
    float regular = get_float("Regular Price: ");
    int percent_off = get_int("What percentage discount: ");
    float sale = dicount(regular, percent_off);
    printf("Sale Price: %.2f\n", sale);
}

float discount(float price, int percentage)
{
    return price * (100 - percentage) / 100;
}