#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int("Pick a number between 0 and 5");
    switch (x)
    {
        case 1:
            printf("You chose the number 1\n");
            break;
        case 2:
            printf("You chose the number 2\n");
            break;
        case 3:
            printf("You chose the number 3\n");
            break;
        case 4:
            printf("You chose the number 4\n");
            break;
        case 5:
            printf("You chose the number 5\n");
            break;

    }
}