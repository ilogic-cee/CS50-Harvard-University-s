#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

// Function prototypes
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Get input from the user
    string text = get_string("Text: ");

    // Count letters, words, and sentences
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

   // Calculate Coleman-Liau index
float L = (float)letters / words * 100;
float S = (float)sentences / words * 100;
int index = (int)(0.0588 * L - 0.296 * S - 15.8); // Round down
if ((0.0588 * L - 0.296 * S - 15.8 - index) >= 0.5)
{
    index++;
}


    // Output the reading level
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }

    return 0;
}

// Implement the count_letters function
int count_letters(string text)
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}

// Implement the count_words function
int count_words(string text)
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isspace(text[i]))
        {
            count++;
        }
        // Check for hyphenated words
        else if (text[i] == '-' && isalpha(text[i - 1]) && isalpha(text[i + 1]))
        {
            continue;
        }
    }
    // Add 1 to account for the last word
    return count + 1;
}

// Implement the count_sentences function
// Implement the count_sentences function
int count_sentences(string text)
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }
    return count;
}
