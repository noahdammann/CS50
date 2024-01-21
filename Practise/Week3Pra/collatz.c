#include <cs50.h>
#include <stdio.h>

int tally = 0;

int collatz(int n);

int main(void)
{
    int num = get_int("Number: ");
    collatz(num);
    printf("%i", n);
}

int collatz(int n)
{

    if (n == 0)
        return 0;
    else if ((n % 2) == 0)
        return 1 + collatz(n/2);
    else
        return 1 + collatz(3*n + 1);
}