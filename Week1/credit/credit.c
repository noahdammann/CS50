#include <cs50.h>
#include <stdio.h>

int i;

int main(void)
{

// Prompt user for card number
double num = get_double("Card number: ");
double card = num;

// Find out how many digits in the card number
for (i = 0; num > 1; i++)
{
        num = num / 10;
}

// Get every 2nd digit
do
{
    if (i % 2 == 0)
    {
        card /= 10
        //array values set to % 10
        i--;
    }
    else
    {
        i--;
    }

}
while (i > 0);

}