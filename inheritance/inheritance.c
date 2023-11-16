#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// ... (rest of the code remains unchanged)

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

// ... (rest of the code remains unchanged)
