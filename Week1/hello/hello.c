#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Get name variable
    string name = get_string("What is your name? ");

    // Say "hello, name"
    printf("hello, %s\n", name);
}