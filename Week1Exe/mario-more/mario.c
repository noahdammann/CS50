#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;

    // Prompt user for height of steps
    do
    {
        n = get_int("Heights: ");
    }
    while (n > 8 || n < 1);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= 2*n + 1; j++)
        {
            // Print spaces between steps
            if (j == n || j == n + 1)
            {
                printf(" ");
            }

            // Print Spaces on left side of left steps
            else if (i + j < n - 1)
            {
                printf(" ");
            }

            // Print right side steps
            else if (i - j > 1/2*n - n - 3)
            {
                printf("#");
            }
        }
        printf("\n");
    }



}