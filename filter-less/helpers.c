#include "bmp.h"
#include "helpers.h"
#include <math.h>

// Function prototypes
RGBTRIPLE get_clamped_sepia_pixel(RGBTRIPLE original_pixel);

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate over each row
    for (int i = 0; i < height; i++)
    {
        // Iterate over each column
        for (int j = 0; j < width; j++)
        {
            // Get sepia-toned pixel based on original pixel values
            RGBTRIPLE sepia_pixel = get_clamped_sepia_pixel(image[i][j]);

            // Update the original pixel with the sepia-toned values
            image[i][j] = sepia_pixel;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate over each row
    for (int i = 0; i < height; i++)
    {
        // Iterate over each column only up to the middle
        for (int j = 0; j < width / 2; j++)
        {
            // Swap pixels from left and right sides horizontally
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
}

// Calculate sepia pixel values based on original pixel values
RGBTRIPLE get_clamped_sepia_pixel(RGBTRIPLE original_pixel)
{
    // Apply sepia formula to calculate new red, green, and blue values
    int sepiaRed = round(.393 * original_pixel.rgbtRed + .769 * original_pixel.rgbtGreen + .189 * original_pixel.rgbtBlue);
    int sepiaGreen = round(.349 * original_pixel.rgbtRed + .686 * original_pixel.rgbtGreen + .168 * original_pixel.rgbtBlue);
    int sepiaBlue = round(.272 * original_pixel.rgbtRed + .534 * original_pixel.rgbtGreen + .131 * original_pixel.rgbtBlue);

    // Clamp values to ensure they are between 0 and 255
    sepiaRed = fmin(255, sepiaRed);
    sepiaGreen = fmin(255, sepiaGreen);
    sepiaBlue = fmin(255, sepiaBlue);

    // Create and return an RGBTRIPLE with the sepia-toned color values
    RGBTRIPLE sepia_pixel;
    sepia_pixel.rgbtRed = sepiaRed;
    sepia_pixel.rgbtGreen = sepiaGreen;
    sepia_pixel.rgbtBlue = sepiaBlue;

    return sepia_pixel;
}
