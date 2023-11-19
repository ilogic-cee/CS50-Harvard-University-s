// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <strings.h>

#include "dictionary.h"

int total_words = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 45;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hash_val;
    node *ptr = NULL;

    hash_val = hash(word);

    ptr=table[hash_val];

    while(ptr != NULL)
    {
        if(strcasecmp(word, ptr->word) == 0)
        {
            return true;
        }
        ptr=ptr->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    int state = 1;
    char buffer[LENGTH+1];
    int hash_val;
    int i = 0;
    node *ptr = NULL;

    FILE *file = fopen(dictionary, "r");
    if(file == NULL)
    {
        fclose(file);
        return false;
    }
    while(state != 0)
    {
        state = fscanf(file,"%s",buffer);
        if(state != 1)
        {
            break;
        }

        node *n = malloc(sizeof(node));

        if(n == NULL)
        {
            fclose(file);
            unload();
            return false;
        }

        n->next = NULL;
        i = 0;

        while(buffer[i] != '\0')
        {
            n->word[i] = buffer[i];
            i++;
        }
        n->word[i] = buffer[i];

        hash_val = hash(n->word);

        n->next = table[hash_val];
        table[hash_val] = n;

    }


    for(int j = 0; j<26; j++)
    {

        ptr=table[j];
        while(ptr != NULL)
        {
        total_words++;
        ptr=ptr->next;
        }
    }

    fclose(file);
    return true;

}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return total_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    int fake = 0;
    node *ptr = NULL;
    node *temp = NULL;

    for(int j = 0; j<26; j++)
    {
        temp=table[j];

        if(temp != NULL)
        {
            ptr = temp->next;
            free(temp);
            temp = ptr;
        }
        free(temp);
    }

    return true;
}