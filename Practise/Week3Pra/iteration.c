#include <stdio.h>
#include <cs50.h>

void print_height(int b);


int main(void)
{
    int n = get_int("Blocks: ");
    print_height(n);
}

void print_height(int b)
{
    for (int i = 0; i < b; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }
    printf("\n");
    }
}