// colorize.c
#include "bmp.h"
#include "helpers.h"

int main(int argc, char *argv[])
{
    // Check for correct number of command-line arguments
    if (argc != 3)
    {
        fprintf(stderr, "Usage: %s infile outfile\n", argv[0]);
        return 1;
    }

    // Open input file
    FILE *infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 2;
    }

    // Open output file
    FILE *outfile = fopen(argv[2], "w");
    if (outfile == NULL)
    {
        fclose(infile);
        fprintf(stderr, "Could not create %s.\n", argv[2]);
        return 3;
    }

    // Your code for reading the input image and calling colorize function goes here

    // Close files
    fclose(infile);
    fclose(outfile);

    return 0;
}
