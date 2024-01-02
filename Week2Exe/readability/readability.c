#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int n;
int letters;
int words;
int sentences;


int count_letters(string sentence);
int count_words(string sentence);
int count_sentences(string sentences);


int main(void)
{
// Prompt user for text
    string text = get_string("Text: ");

// Calculate the length of the text
    n = strlen(text);

// Perform functions
    count_letters(text);
    count_words(text);
    count_sentences(text);

// Calculate L and S
    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;

// Perfrom grade calculation
    float index = 0.0588 * L - 0.296 * S - 15.8;

// Print results
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.0f\n", index);
    }
}

// Count the letters in the text
int count_letters(string user_input)
{
    letters = 0;
    for (int i = 0; i < n; i++)
    {
        if (isupper(user_input[i]))
        {
            letters += 1;
        }
        if (islower(user_input[i]))
        {
            letters += 1;
        }
    }
    return letters;
}


// Count the words in the text
int count_words(string user_input)
{
    words = 0;
    for (int i = 0; i < n; i++)

        if (isspace(user_input[i]))
        {
            words += 1;
        }
    words += 1;
    return words;
}


// Count the sentences in the text
int count_sentences(string user_input)
{
    sentences = 0;
    for (int i = 0; i < n ; i++)
    {

        if (user_input[i] == '.' || user_input[i] == '!' || user_input[i] == '?')
        {
            sentences += 1;
        }
    }
    return sentences;
}