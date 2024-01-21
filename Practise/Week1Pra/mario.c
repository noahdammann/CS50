#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    while (true)
    {
        n = get_int("Size: ");
        if (n > 0)
        {
            break;
        }
    }


    // For each column
    for (int i = 0; i < n; i++)
    {

        // For each row
        for (int j = 0; j < n; j++)
        {
        printf("#");
        }

    // Move to next row
    printf("\n");

    }
printf("\n");
}