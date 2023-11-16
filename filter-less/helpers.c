#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "bmp.h"
#include "helpers.h"

// Function prototypes
RGBTRIPLE get_clamped_sepia_pixel(RGBTRIPLE original_pixel);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate over each row
    for (int i = 0; i < height; i++)
    {
        // Iterate over each column
        for (int j = 0; j < width; j++)
        {
            // Calculate average of red, green, and blue values
            BYTE average = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3;

            // Set each color channel to the calculated average
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
}



// Convert image to sepia
// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate over each row
    for (int i = 0; i < height; i++)
    {
        // Iterate over each column
        for (int j = 0; j < width; j++)
        {
            // Calculate sepia values based on original color values
            int sepiaRed = round(0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);

            // Clamp values to ensure they are between 0 and 255
            sepiaRed = MIN(sepiaRed, 255);
            sepiaGreen = MIN(sepiaGreen, 255);
            sepiaBlue = MIN(sepiaBlue, 255);

            // Update the original pixel with sepia-toned values
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
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




// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a temporary copy of the image to store the blurred values
    RGBTRIPLE(*temp)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    if (temp == NULL)
    {
        fprintf(stderr, "Not enough memory to store temporary image.\n");
        exit(1);
    }

    // Iterate over each row
    for (int i = 0; i < height; i++)
    {
        // Iterate over each column
        for (int j = 0; j < width; j++)
        {
            int totalRed = 0;
            int totalGreen = 0;
            int totalBlue = 0;
            int validNeighbors = 0;

            // Iterate over the 3x3 grid centered on the current pixel
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    // Check if the neighbor is within the image boundaries
                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        // Accumulate color values
                        totalRed += image[ni][nj].rgbtRed;
                        totalGreen += image[ni][nj].rgbtGreen;
                        totalBlue += image[ni][nj].rgbtBlue;
                        validNeighbors++;
                    }
                }
            }

            // Calculate average values and store in temporary image
            temp[i][j].rgbtRed = round((float)totalRed / validNeighbors);
            temp[i][j].rgbtGreen = round((float)totalGreen / validNeighbors);
            temp[i][j].rgbtBlue = round((float)totalBlue / validNeighbors);
        }
    }

    // Copy the blurred values back to the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }

    // Free memory for the temporary image
    free(temp);
}

// Detect edges in image
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a temporary copy of the image to store the new pixel values
    RGBTRIPLE(*temp)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    if (temp == NULL)
    {
        fprintf(stderr, "Not enough memory to store temporary image.\n");
        exit(1);
    }

    // Sobel operator for edge detection
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    // Iterate over each row
    for (int i = 0; i < height; i++)
    {
        // Iterate over each column
        for (int j = 0; j < width; j++)
        {
            int Gx_red = 0, Gx_green = 0, Gx_blue = 0;
            int Gy_red = 0, Gy_green = 0, Gy_blue = 0;

            // Iterate over the 3x3 grid centered on the current pixel
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    // Check if the neighbor is within the image boundaries
                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        Gx_red += Gx[di + 1][dj + 1] * image[ni][nj].rgbtRed;
                        Gx_green += Gx[di + 1][dj + 1] * image[ni][nj].rgbtGreen;
                        Gx_blue += Gx[di + 1][dj + 1] * image[ni][nj].rgbtBlue;

                        Gy_red += Gy[di + 1][dj + 1] * image[ni][nj].rgbtRed;
                        Gy_green += Gy[di + 1][dj + 1] * image[ni][nj].rgbtGreen;
                        Gy_blue += Gy[di + 1][dj + 1] * image[ni][nj].rgbtBlue;
                    }
                }
            }

            // Calculate combined gradient magnitude
            int red = round(sqrt(Gx_red * Gx_red + Gy_red * Gy_red));
            int green = round(sqrt(Gx_green * Gx_green + Gy_green * Gy_green));
            int blue = round(sqrt(Gx_blue * Gx_blue + Gy_blue * Gy_blue));

            // Clamp values to ensure they are between 0 and 255
            red = fmin(255, red);
            green = fmin(255, green);
            blue = fmin(255, blue);

            // Update the temporary image with the new values
            temp[i][j].rgbtRed = red;
            temp[i][j].rgbtGreen = green;
            temp[i][j].rgbtBlue = blue;
        }
    }

    // Copy the edge-detected values back to the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }

    // Free memory for the temporary image
    free(temp);
}
