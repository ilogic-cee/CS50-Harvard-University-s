#include <stdio.h>
#include <stdlib.h>

// Define the possible alleles for blood types
typedef enum
{
    A,
    B,
    O
} Allele;

// Define a struct to represent a person
typedef struct person
{
    struct person *parents[2]; // Array to store two parents
    Allele alleles[2];         // Array to store two alleles
} Person;

// Function to generate a random allele (A, B, or O)
Allele random_allele()
{
    int random = rand() % 3;
    switch (random)
    {
    case 0:
        return A;
    case 1:
        return B;
    default:
        return O;
    }
}

// Function to create a family of a specified number of generations
Person *create_family(int generations)
{
    // Allocate memory for a new person
    Person *new_person = malloc(sizeof(Person));

    // Check if there are more generations to create
    if (generations > 1)
    {
        // Recursively create parents for the new person
        Person *parent0 = create_family(generations - 1);
        Person *parent1 = create_family(generations - 1);

        // Set the parent pointers of the new person
        new_person->parents[0] = parent0;
        new_person->parents[1] = parent1;

        // Assign alleles for the new person by randomly choosing one allele from each parent
        new_person->alleles[0] = parent0->alleles[rand() % 2];
        new_person->alleles[1] = parent1->alleles[rand() % 2];
    }
    else
    {
        // Base case: no more generations, so no parents
        new_person->parents[0] = NULL;
        new_person->parents[1] = NULL;

        // Assign random alleles for the new person
        new_person->alleles[0] = random_allele();
        new_person->alleles[1] = random_allele();
    }

    // Return a pointer to the created person
    return new_person;
}

// Function to free the memory allocated for a family
void free_family(Person *p)
{
    // Base case: if the input is NULL, return immediately
    if (p == NULL)
    {
        return;
    }

    // Recursively free memory for both parents before freeing the child
    free_family(p->parents[0]);
    free_family(p->parents[1]);

    // Free the memory for the current person
    free(p);
}

// Function to print the family tree
void print_family(Person *p, int level)
{
    if (p == NULL)
    {
        return;
    }

    // Print the current person's blood type and generation
    printf("%*s", level * 4, ""); // Adjust indentation
    printf("Child (Generation %d): blood type ", level);
    switch (p->alleles[0])
    {
    case A:
        printf("A");
        break;
    case B:
        printf("B");
        break;
    case O:
        printf("O");
        break;
    }

    switch (p->alleles[1])
    {
    case A:
        printf("A\n");
        break;
    case B:
        printf("B\n");
        break;
    case O:
        printf("O\n");
        break;
    }

    // Recursively print parents
    for (int i = 0; i < 2; i++)
    {
        if (p->parents[i] != NULL)
        {
            printf("%*s", (level + 1) * 4, ""); // Adjust indentation
            printf("Parent (Generation %d): blood type ", level + 1);
            switch (p->parents[i]->alleles[0])
            {
            case A:
                printf("A");
                break;
            case B:
                printf("B");
                break;
            case O:
                printf("O");
                break;
            }

            switch (p->parents[i]->alleles[1])
            {
            case A:
                printf("A\n");
                break;
            case B:
                printf("B\n");
                break;
            case O:
                printf("O\n");
                break;
            }

            // Recursively print grandparents
            for (int j = 0; j < 2; j++)
            {
                if (p->parents[i]->parents[j] != NULL)
                {
                    printf("%*s", (level + 2) * 4, ""); // Adjust indentation
                    printf("Grandparent (Generation %d): blood type ", level + 2);
                    switch (p->parents[i]->parents[j]->alleles[0])
                    {
                    case A:
                        printf("A");
                        break
