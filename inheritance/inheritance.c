#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Enum for blood types
typedef enum
{
    A,
    B,
    O
} Allele;

// Struct to represent a person
typedef struct person
{
    Allele alleles[2];           // Blood type alleles
    struct person *parents[2];   // Pointers to parents
} Person;

// Function prototypes
Person *create_family(int generations);
void free_family(Person *p);
void print_family(const Person *p);

// Function to generate a random allele
Allele random_allele(void)
{
    int r = rand() % 3;
    switch (r)
    {
    case 0:
        return A;
    case 1:
        return B;
    default:
        return O;
    }
}

// TODO: Implement create_family function
Person *create_family(int generations)
{
    // Allocate memory for a new person
    Person *p = malloc(sizeof(Person));

    // Base case: no more generations
    if (generations == 1)
    {
        p->parents[0] = NULL;
        p->parents[1] = NULL;
        p->alleles[0] = random_allele();
        p->alleles[1] = random_allele();
    }
    else
    {
        // Recursive case: create parents and assign alleles
        p->parents[0] = create_family(generations - 1);
        p->parents[1] = create_family(generations - 1);
        p->alleles[0] = random_allele();
        p->alleles[1] = random_allele();
    }

    return p;
}

// TODO: Implement free_family function
void free_family(Person *p)
{
    // Base case: person is NULL
    if (p == NULL)
    {
        return;
    }

    // Recursive case: free parents and then free the person
    free_family(p->parents[0]);
    free_family(p->parents[1]);
    free(p);
}

// TODO: Implement print_family function
void print_family(const Person *p)
{
    // Your code for printing the family tree goes here
    if (p != NULL)
    {
        // Print the child's blood type
        printf("Child (Generation 0): blood type ");
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
            printf("A");
            break;
        case B:
            printf("B");
            break;
        case O:
            printf("O");
            break;
        }

        printf("\n");

        // Print parents' blood types
        for (int i = 0; i < 2; i++)
        {
            if (p->parents[i] != NULL)
            {
                printf("    Parent (Generation 1): blood type ");
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
                    printf("A");
                    break;
                case B:
                    printf("B");
                    break;
                case O:
                    printf("O");
                    break;
                }

                printf("\n");

                // Print grandparents' blood types
                for (int j = 0; j < 2; j++)
                {
                    if (p->parents[i]->parents[j] != NULL)
                    {
                        printf("        Grandparent (Generation 2): blood type ");
                        switch (p->parents[i]->parents[j]->alleles[0])
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

                        switch (p->parents[i]->parents[j]->alleles[1])
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

                        printf("\n");
                    }
                }
            }
        }
    }
}

int main(void)
{
    // Seed the random number generator
    srand(time(NULL));

    // Create a family with 3 generations
    Person *family = create_family(3);

    // Print the family tree
    print_family(family);

    // Free the allocated memory
    free_family(family);

    return 0;
}
