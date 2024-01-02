#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool check_valid(string s);
bool check_repeats(string s);

int status;
string str;
string index;

int main(int argc, string argv[])
{
// Check command line-arguement is valid

    // Arguement contains only 2 inputs
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    // If key isn't 26 characters
    if (!check_valid(argv[1]))
    {
        printf("Key must contain 26 characters\n");
        return 1;
    }
    // If key contains repeat characters
    if (!check_repeats(argv[1]))
    {
        printf("Key must not contain repeated characters\n");
        return 1;
    }

// Get plaintext
    printf("plaintext:  ");
    str = get_string("");

// Encipher plaintext
    printf("ciphertext: ");
    index = argv[1];
    for (int i = 'A'; i <= 'Z'; i++)
    {
        index[i - 'A'] = toupper(index[i - 'A']) - i;
    }
    for (int i = 0; i < strlen(str); i++)
    {
        if (isalpha(str[i]))
        {
            str[i] = str[i] + index[str[i] - (isupper(str[i]) ? 'A' : 'a')];
        }
    printf("%c", str[i]);
    }
    printf("\n");


}

// Function to check for valid key
bool check_valid(string s)
{
    // Check that it is 26 characters
    int n = strlen(s);
    if (n != 26)
    {
        return false;
    }
    // Check to see if it contains a digit
    for (int i = 0; i < n; i++)
    {
        if (!isalpha(s[i]))
        {
            return false;
        }
    }
    // Check to see if it contains repeat letters

    return true;
}

bool check_repeats(string s)
{
    for (int i = 0; i < strlen(s); i++)
    {

        for (int j = (i - 1); j >= 0; j--)
        {
            if ((s[i] - s[j]) == 0)
            {
                return false;
            }
        }
    }
    return true;
}

