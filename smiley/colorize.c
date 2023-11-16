#include <stdio.h>
#include <stdlib.h>
#include "bmp.h"

void colorize(int height, int width, RGBTRIPLE image[height][width]);

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 3)
    {
        fprintf(stderr, "Usage: %s infile outfile\n", argv[0]);
        return 1;
    }

    // Open input file
    FILE *infile = fopen(argv[1], "rb");
    if (infile == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 2;
    }

    // Open output file
    FILE *outfile = fopen(argv[2], "wb");
    if (outfile == NULL)
    {
        fclose(infile);
        fprintf(stderr, "Could not create %s.\n", argv[2]);
        return 3;
    }

    // Read BMP headers
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, infile);

    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, infile);

    // Allocate memory for image
    int height = abs(bi.biHeight);
    int width = bi.biWidth;
    RGBTRIPLE (*image)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    if (image == NULL)
    {
        fclose(outfile);
        fclose(infile);
        fprintf(stderr, "Not enough memory to store image.\n");
        return 4;
    }

    // Read pixels from input file
    for (int i = 0; i < height; i++)
    {
        fread(image[i], sizeof(RGBTRIPLE), width, infile);
        fseek(infile, padding, SEEK_CUR);
    }

    // Call colorize function
    colorize(height, width, image);

    // Write BMP headers to output file
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outfile);
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outfile);

    // Write modified pixels to output file
    for (int i = 0; i < height; i++)
    {
        fwrite(image[i], sizeof(RGBTRIPLE), width, outfile);

        for (int k = 0; k < padding; k++)
        {
            fputc(0x00, outfile);
        }
    }

    // Free allocated memory
    free(image);

    // Close files
    fclose(infile);
    fclose(outfile);

    return 0;
}
