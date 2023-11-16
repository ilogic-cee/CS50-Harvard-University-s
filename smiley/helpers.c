#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>  // Include cs50.h for user input functions
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

    // ... (rest of your main function logic)

    return 0;
}

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Define the color you want to use for non-black pixels
    RGBTRIPLE newColor;
    newColor.rgbtRed = 255;    // Red component
    newColor.rgbtGreen = 255;  // Green component
    newColor.rgbtBlue = 255;   // Blue component

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
