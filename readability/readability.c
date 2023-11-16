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
    int index = (int)(0.0588 * L - 0.296 * S - 15.8);

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
    // TODO: Implement counting of letters in the text
    // You can use isalpha() function to check if a character is a letter
}

// Implement the count_words function
int count_words(string text)
{
    // TODO: Implement counting of words in the text
    // You may need to iterate through characters and count spaces
}

// Implement the count_sentences function
int count_sentences(string text)
{
    // TODO: Implement counting of sentences in the text
    // You can consider '.', '!', '?' as sentence-ending punctuation
}
