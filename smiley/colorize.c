// colorize.c
#include <stdio.h>
#include <stdlib.h>
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

    // Read the BMP file headers (you may need to adjust this based on your specific headers)
    BITMAPFILEHEADER bf;
    BITMAPINFOHEADER bi;

    fread(&bf, sizeof(BITMAPFILEHEADER), 1, infile);
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, infile);

    // Create a 2D array to store the image pixels
    RGBTRIPLE(*image)[bi.biWidth] = calloc(abs(bi.biHeight), sizeof(RGBTRIPLE[bi.biWidth]));
    if (image == NULL)
    {
        fclose(infile);
        fclose(outfile);
        fprintf(stderr, "Not enough memory to store image.\n");
        return 4;
    }

    // Read the image pixels
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {
        fread(image[i], sizeof(RGBTRIPLE), bi.biWidth, infile);
        fseek(infile, bi.biWidth * sizeof(RGBTRIPLE), SEEK_CUR);
    }

    // Call the colorize function to change pixel colors
    colorize(abs(bi.biHeight), bi.biWidth, image);

    // Write the modified headers to the output file
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outfile);
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outfile);

    // Write the modified image pixels to the output file
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {
        fwrite(image[i], sizeof(RGBTRIPLE), bi.biWidth, outfile);

        // Add padding if necessary (you may need to adjust this based on your specific headers)
        for (int k = 0; k < (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4; k++)
        {
            fputc(0x00, outfile);
        }
    }

    // Close files and free memory
    fclose(infile);
    fclose(outfile);
    free(image);

    return 0;
}
