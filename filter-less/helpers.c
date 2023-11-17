#include "helpers.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "bmp.h"


// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

            // convert pixel to float
            // BYTE gray = (BYTE)(0.299 * image[i][j].rgbtRed + 0.587 * image[i][j].rgbtGreen + 0.114 * image[i][j].rgbtBlue);
            float image[i][j].rgbtRed ;
            float image[i][j].rgbtGreen ;
            float image[i][j].rgbtBlue ;

        int average = round((Red + Green + Blue)/3);
        image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = average ;
        }

    }
    return;
}

// Convert image to sepia


/* Helper function to cap the color values at 255
int cap(int value)
{
    return value > 255 ? 255 : value;
}
*/

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate over each pixel in the image

    //  comb through each row
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Calculate sepia values
            // Convert pixels to float

            float originalRed = image[i][j].rgbtRed;
            float originalGreen = image[i][j].rgbtGreen;
            float originalBlue = image[i][j].rgbtBlue;


            int sepiaRed = round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue);
            int sepiaGreen = round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue);
            int sepiaBlue = round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);

            // Update pixel values with sepia values
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
             {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255 ;
            }


            // Update final pixel values

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return; 
}

// Reflect image horizontally


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


// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a temporary image to store the blurred result
    RGBTRIPLE(*temp_image)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    if (temp_image == NULL)
    {
        printf("Not enough memory to store temporary image.\n");
        return;
    }

    // Iterate over each pixel in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumRed = 0, sumGreen = 0, sumBlue = 0;
            int count = 0;

            // Iterate over the neighboring pixels (3x3 grid centered on the current pixel)
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    // Check if the neighboring pixel is within bounds
                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        // Accumulate the RGB values of neighboring pixels
                        sumRed += image[ni][nj].rgbtRed;
                        sumGreen += image[ni][nj].rgbtGreen;
                        sumBlue += image[ni][nj].rgbtBlue;
                        count++;
                    }
                }
            }

            // Calculate the average RGB values and update the temporary image
            temp_image[i][j].rgbtRed = round((float)sumRed / count);
            temp_image[i][j].rgbtGreen = round((float)sumGreen / count);
            temp_image[i][j].rgbtBlue = round((float)sumBlue / count);
        }
    }

    // Copy the blurred result back to the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp_image[i][j];
        }
    }

    // Free memory for the temporary image
    free(temp_image);
}
