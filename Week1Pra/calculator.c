#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Prompt user for x
    int x = get_int("x: ");

    //Prompt user for y
    int y = get_int("y: ");

    //Make z
    float z = (float) x / (float) y;

    //Perform division
    printf("%f\n", z);
}
