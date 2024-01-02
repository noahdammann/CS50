#include <cs50.h>
#include <stdio.h>

int main(void)
{
    const int MINE = 2;
    int points = get_int("how many points did you lose? ");

    if (points > MINE)
    {
        printf("You lost more points than me\n");
    }
    else if (points < MINE)
    {
        printf("You lost less points than me\n");
    }
    else
    {
        printf("You lost the same amount of points as me\n");
    }
}