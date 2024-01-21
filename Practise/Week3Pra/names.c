#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string names[] = {"Andrew", "Simon", "Peter", "John", "Philip", "Matthew", "Judas", "Bartholomew", "James", "Thomas", "James", "Thaddaeus"};

    for (int i = 0; i < 12; i++)
    {
        if (strcmp(names[i], "Mark") == 0)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}