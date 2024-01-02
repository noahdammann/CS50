#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int num;
int shift;
int key;
bool status;
char rotate;

bool only_digits(string user_input);

int main(int argc, string argv[])
{
    // Reject command line inputs that are longer or shorter than 1 arguement
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Make sure argv[1] is a digit
    only_digits(argv[1]);
    if (status == 0)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }


    // Convert command line input to integer
    key = atoi(argv[1]);
    printf("%i\n", key);

    // Prompt user for input
    string plaintext = get_string(" plaintext: ");
    printf("ciphertext: ");

    // Rotate each char
    for (int i = 0; i < strlen(plaintext); i++)
    {
        // If uppercase
        if (isupper(plaintext[i]))
        {
            printf("%c", (plaintext[i] - 65 + key) % 26 + 65);
        }
        // If lowercase
        else if (islower(plaintext[i]))
        {
            printf("%c", (plaintext[i] - 97 + key) % 26 + 97);
        }
        // If non-alphabetical
        else
        {
            printf("%c", plaintext[i]);
        }

    }
    printf("\n");
}

// Function to check that argv[1] is a digit
bool only_digits(string user_input)
{
    for (int i = 0, n = strlen(user_input); i < n; i++)
    {
        if (isdigit(user_input[i]))
        {
            status = 1;
        }
        else
        {
            status = 0;
            break;
        }

    }
    return status;
}

