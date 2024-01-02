#include <cs50.h>
#include <stdio.h>

int main(void)
{

int n;

// Get Height
do
{
    n = get_int("Height: ");
}
while (n < 1 || n > 8);

// Rows
for (int i = 0; i < n; i++)
    {

    // Columns
    for (int j = 0; j < n; j++)
    {
        if (i + j < n - 1)
        {
            printf(" ");
        }
        else
        {
            printf("#");
        }
    }
        printf("\n");
    }
}