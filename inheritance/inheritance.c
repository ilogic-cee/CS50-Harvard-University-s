#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Define the possible blood types
typedef enum
{
    A,
    B,
    O
} BloodType;

// Define the structure for a person
typedef struct Person
{
    struct Person *parents[2];
    BloodType alleles[2];
} Person;

// Function prototypes
Person *create_family(int generations);
void print_family(const Person *p);
void free_family(Person *p);

// Function to generate a random allele
BloodType random_allele(void)
{
    int r = rand() % 3;
    return (BloodType)r;
}

// Function to create a family tree
Person *create_family(int generations)
{
    // Allocate memory for a new person
    Person *p = malloc(sizeof(Person));

    // Check if there are more generations to create
    if (generations > 1)
    {
        // Recursively create parents
        Person *parent0 = create_family(generations - 1);
        Person *parent1 = create_family(generations - 1);

        // Set the parents for the current person
        p->parents[0] = parent0;
        p->parents[1] = parent1;

        // Assign alleles randomly from parents
        p->alleles[0] = parent0->alleles[rand() % 2];
        p->alleles[1] = parent1->alleles[rand() % 2];
    }
    else
    {
        // No more generations, set parents to NULL
        p->parents[0] = NULL;
        p->parents[1] = NULL;

        // Assign random alleles
        p->alleles[0] = random_allele();
        p->alleles[1] = random_allele();
    }

    return p;
}

// Function to print the family tree
void print_family(const Person *p)
{
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

// Function to free memory allocated for the family tree
void free_family(Person *p)
{
    if (p != NULL)
    {
        // Recursively free parents
        free_family(p->parents[0]);
        free_family(p->parents[1]);

        // Free the current person
        free(p);
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

    // Free memory
    free_family(family);

    return 0;
}
