#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char *s = malloc(5);
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}