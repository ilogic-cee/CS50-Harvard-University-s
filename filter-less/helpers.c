#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            BYTE gray = (BYTE)(0.299 * image[i][j].rgbtRed + 0.587 * image[i][j].rgbtGreen + 0.114 * image[i][j].rgbtBlue);
            image[i][j].rgbtRed = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtBlue = gray;
        }
    }
}

// Convert image to sepia
#include "helpers.h"

// Helper function to cap the color values at 255
int cap(int value)
{
    return value > 255 ? 255 : value;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate over each pixel in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Calculate sepia values
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            int sepiaRed = cap(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue);
            int sepiaGreen = cap(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue);
            int sepiaBlue = cap(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);

            // Update pixel values with sepia values
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
}

// Reflect image horizontally
#include "helpers.h"

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate over each row in the image
    for (int i = 0; i < height; i++)
    {
        // Iterate over each column in the row up to the center
        for (int j = 0; j < width / 2; j++)
        {
            // Swap pixels with their corresponding pixels on the other side
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
}


// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
