// ... (previous code)

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Declare padding
    int padding = (4 - (width * sizeof(RGBTRIPLE)) % 4) % 4;

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

// ... (rest of the code)
