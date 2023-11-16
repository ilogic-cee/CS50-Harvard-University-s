// colorize.c
#include <stdio.h>
#include <stdlib.h>
#include "bmp.h"

void colorize(int height, int width, RGBTRIPLE image[height][width]);

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        fprintf(stderr, "Usage: %s infile outfile\n", argv[0]);
        return 1;
    }

    // Open input file
    FILE *inptr = fopen(argv[1], "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 2;
    }

    // Open output file
    FILE *outptr = fopen(argv[2], "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", argv[2]);
        return 3;
    }

    // Read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // Read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // Ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    int height = abs(bi.biHeight);
    int width = bi.biWidth;

    // Allocate memory for image
    RGBTRIPLE (*image)[width] = calloc(height, sizeof(RGBTRIPLE[width]));
    if (image == NULL)
    {
        fprintf(stderr, "Not enough memory to store image.\n");
        fclose(outptr);
        fclose(inptr);
        return 5;
    }

    // ... (rest of your main function logic)

    return 0;
}

// ... (unchanged code)

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Define the color you want to use for non-black pixels
    RGBTRIPLE newColor;
    newColor.rgbtRed = 255;    // Red component
    newColor.rgbtGreen = 0;    // Green component
    newColor.rgbtBlue = 0;     // Blue component

    // Iterate through each pixel in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Check if the pixel is black (assuming RGB values 0, 0, 0)
            if (image[i][j].rgbtBlue == 0 && image[i][j].rgbtGreen == 0 && image[i][j].rgbtRed == 0)
            {
                // Change the color of black pixels
                image[i][j] = newColor;
            }
        }
    }
}
