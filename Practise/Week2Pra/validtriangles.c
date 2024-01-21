#include <stdio.h>
#include <cs50.h>

bool check_triangle(int a, int b, int c);

int main(void)
{
int x = get_int("What is the length of the first side of your triangle?");
int y = get_int("What is the length of the second side of your triangle?");
int z = get_int("What is the length of the third side of your triangle?");

// Check if triangle is valid
bool check_triangle(int x, int y, int z);
if (bool true)
    {
        printf("True\n");
    }
else
    {
        printf("False\n");
    }
}

bool check_triangle(int a, int b, int c)
{
    if (a <= 0 || b <= 0 || c <= 0)
    {
        return false;
    }

    if (a > 2*(b + c) || b > 2*(a + c) || c > 2*(a + b))
    {
        return false;
    }
    else
    return true;

}