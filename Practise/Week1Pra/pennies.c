#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float dollar = get_float("Dollar amount: ");
    int pennies = round(dollar * 100);
    printf("%i\n", pennies);
}