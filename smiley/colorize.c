// colorize.c
#include <stdio.h>
#include <stdlib.h>
#include "bmp.h"

void colorize(int height, int width, RGBTRIPLE image[height][width]);

int main(int argc, char *argv[])
{
    // ... (unchanged code)

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 6;
    }

    int height = abs(bi.biHeight);  // Use abs for absolute value
    int width = bi.biWidth;

    // allocate memory for image
    RGBTRIPLE (*image)[width] = calloc(abs(bi.biHeight), sizeof(RGBTRIPLE[bi.biWidth]));

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
